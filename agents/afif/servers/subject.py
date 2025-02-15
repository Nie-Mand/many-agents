from mcp.server.fastmcp import FastMCP

mcp = FastMCP("subject")

@mcp.tool()
def get_chapters() -> list:
    """
    Get the chapters of the course.
    """
    return [
        "Introduction",
        "The Basics",
        "Advanced Topics",
        "Conclusion"
    ]

@mcp.tool()
def get_chapter_content(chapter: str) -> str:
    """
    Get the content of a chapter.
    Args:
        chapter (str): The chapter to get the content of.
    """
    if chapter == "Introduction":
        return "3G, 4G, 5G"
    elif chapter == "The Basics":
        return "IMSU Protocol"
    elif chapter == "Advanced Topics":
        return "This is the advanced topics chapter."
    elif chapter == "Conclusion":
        return "This is the conclusion chapter."
    else:
        return "Chapter not found."

if __name__ == "__main__":
    mcp.run(transport='stdio')
