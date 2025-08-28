import asyncio
from agents import Agent , Runner , function_tool , RunContextWrapper 
from connection import config
from pydantic import BaseModel
import rich


class LibraryBook(BaseModel):
    book_id: str
    book_title: str
    author_name:str
    is_available: bool
# -------------------
library_book = LibraryBook(
    book_id="BOOK-123",
    book_title="Python Programming",
    author_name="John Smith",
    is_available=True
)
# --------------------
@function_tool
def get_library_book_info(wrapper: RunContextWrapper[LibraryBook]):
    book = wrapper.context
    return (
        f"Library Book Details:\n"
        f"- Book ID: {book.book_id}\n"
        f"- Title: {book.book_title}\n"
        f"- Author: {book.author_name}\n"
        f"- Available: {'Yes' if book.is_available else 'No'}"
    )
# --------------------


library_book_agent = Agent[LibraryBook](
    name="Agent",
    instructions="You are a helpful assistant, always call the tool to get library book details",
    tools=[get_library_book_info]
)
# -------------------

async def main():
    result = await Runner.run(
        starting_agent= library_book_agent,
        input="Tell me the library book details",
        run_config=config,
        context=library_book 
    )
    rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
