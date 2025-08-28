import asyncio
from agents import Agent , Runner , function_tool , RunContextWrapper 
from connection import config
from pydantic import BaseModel
import rich


class StudentProfile(BaseModel):
    student_id:str
    student_name:str
    current_semester:int
    total_courses:int
# -------------------
student = StudentProfile(
    student_id="STU-456",
    student_name="Hassan Ahmed",
    current_semester=4,
    total_courses=5
)
# --------------------
@function_tool
def get_student_info(wrapper: RunContextWrapper[StudentProfile]):
    student = wrapper.context
    return (
        f"Student Details:\n"
        f"- Student Name: {student.student_name}\n"
        f"- Student ID: {student.student_id}\n"
        f"- Current Semester: {student.current_semester}\n"
        f"- Total Courses: {student.total_courses}"
    )

# --------------------


student_agent = Agent[StudentProfile](
    name="Agent",
    instructions="You are a helpful assistant, always call the tool to get student details",
    tools=[get_student_info]
)
# -------------------

async def main():
    result = await Runner.run(
        starting_agent= student_agent,
        input="Tell me the student details",
        run_config=config,
        context=student 
    )
    rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
