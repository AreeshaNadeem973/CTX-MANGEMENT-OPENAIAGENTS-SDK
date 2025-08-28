import asyncio
from agents import Agent , Runner , function_tool , RunContextWrapper 
from connection import config
from pydantic import BaseModel
import rich


class BankAccount(BaseModel):
    account_number:str
    customer_name:str
    account_balance:float
    account_type:str

# -------------------
bank_account = BankAccount(
    account_number="ACC-789456",
    customer_name="Fatima Khan",
    account_balance=75500.50,
    account_type="savings"
)
# --------------------
@function_tool
def get_bank_info(wrapper: RunContextWrapper[BankAccount]):
    account = wrapper.context
    return (
        f"Account Details:\n"
        f"- Customer Name: {account.customer_name}\n"
        f"- Account Number: {account.account_number}\n"
        f"- Account Type: {account.account_type}\n"
        f"- Balance: {account.account_balance} PKR"
    )
# --------------------


bank_agent = Agent[BankAccount](
    name="Agent",
    instructions="You are a helpful assistant, always call the tool to get bank account details",
    tools=[get_bank_info]
)
# -------------------

async def main():
    result = await Runner.run(
        starting_agent= bank_agent,
        input="Tell me the account details",
        run_config=config,
        context=bank_account
    )
    rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
