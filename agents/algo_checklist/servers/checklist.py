from mcp.server.fastmcp import FastMCP

mcp = FastMCP("checklist")

@mcp.tool()
def get_current_level() -> str:
    """
    Get the current level of the user.
    """
    return "Beginner"

@mcp.tool()
def get_lists() -> list:
    """
    Get the lists of problems collections
    """
    return [
        {
            "id": "leetcode-75",
            "name": "LeetCode Top 75",
            "url": "https://leetcode.com/problemset/top-75/"
        },
        {
            "id": "leetcode-100",
            "name": "LeetCode Top 100",
            "url": "https://leetcode.com/problemset/top-100/"
        }
    ]

@mcp.tool()
def get_problems(selected_list: str) -> list:
    """
    Get problems based on the current level of the user, from the selected list.
    Args:
        selected_list (str): The selected list of problems.
    """

    list = [
        {
                "id": "475",
                "list": "leetcode-75",
                "name": "LinkedList",
                "url": "https://leetcode.com/problemset/top-75/2",
                "level": "Medium"
            },
            {
                "id": "47s5",
                "list": "leetcode-75",
                "name": "Hello, Wolrd",
                "url": "https://leetcode.com/problemset/top-75/2",
                "level": "Beginner"
            },
    ]

    return [problem for problem in list if problem["level"] == "Beginner"]

@mcp.tool()
def mark_problem_as_done(problem_id: str) -> str:
    """
    Mark a problem as done.
    Args:
        problem_id (str): The id of the problem to mark as done.
    """

    return "Done"

@mcp.tool()
def how_many_problems_solved() -> int:
    """
    Get the number of problems solved.
    """

    return 2


if __name__ == "__main__":
    mcp.run(transport='stdio')
