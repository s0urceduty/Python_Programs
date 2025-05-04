# Sourceduty Notepad V3.0-Update
# Copyright (C) 2024, Sourceduty

# Default settings for the text editor
DEFAULT_FONT = ("Arial", 12)
DEFAULT_THEME = "light"  # Can be "light" or "dark"

# Utility function to set theme
def set_theme(editor, theme):
    if theme == "dark":
        editor.text_area.config(bg="black", fg="white")
    else:
        editor.text_area.config(bg="white", fg="black")

# Utility function to set font
def set_font(editor, font_name="Arial", font_size=12):
    editor.text_area.config(font=(font_name, font_size))

# Templates for various document types
TEMPLATES = {
    "Book Index": (
        "CONTENTS\n\n"
        "Chapter 1 ............................... 1\n"
        "Chapter 2 ............................... 14\n"
        "Chapter 3 ............................... 23\n"
        "Chapter 4 ............................... 43\n"
        "Chapter 5 ............................... 56\n"
        "Chapter 6 ............................... 75\n"
        "Chapter 7 ............................... 78\n"
        "Chapter 8 ............................... 92\n"
        "Chapter 9 ............................... 101\n"
    ),
    "Invoice": (
        "Invoice\n"
        "------------------------------------\n"
        "Item Description      Quantity    Price\n"
        "------------------------------------\n"
        "Widget A                10       $2.99\n"
        "Widget B                5        $3.99\n"
        "------------------------------------\n"
        "Total:                             $49.85\n"
    ),
    "Instructions": (
        "Instructions for Building a Bookshelf\n"
        "-------------------------------------\n"
        "1. Gather all materials and tools.\n"
        "2. Assemble the sides, top, and bottom.\n"
        "3. Attach the back panel.\n"
        "4. Insert the shelves.\n"
        "5. Sand and finish as desired.\n"
    ),
    "Recipe": (
        "Recipe: Chocolate Chip Cookies\n"
        "Ingredients:\n"
        "- 2 1/4 cups all-purpose flour\n"
        "- 1/2 tsp baking soda\n"
        "- 1 cup unsalted butter, room temperature\n"
        "- 1/2 cup granulated sugar\n"
        "- 1 cup packed light-brown sugar\n"
        "- 1 tsp salt\n"
        "- 2 tsp pure vanilla extract\n"
        "- 2 large eggs\n"
        "- 2 cups semisweet and/or milk chocolate chips\n"
        "Instructions:\n"
        "- Preheat oven to 350 degrees.\n"
        "- In a small bowl, whisk together the flour and baking soda; set aside.\n"
        "- Combine the butter with both sugars; beat on medium speed until light and fluffy.\n"
        "- Reduce speed to low; add the salt, vanilla, and eggs. Beat until well mixed.\n"
        "- Add the flour mixture; mix until just combined.\n"
        "- Stir in the chocolate chips.\n"
        "- Drop heaping tablespoon-size balls of dough about 2 inches apart on baking sheets.\n"
        "- Bake until cookies are golden around the edges but still soft in the center, 8 to 10 minutes.\n"
        "- Remove from oven, and let cool on baking sheet 1 to 2 minutes.\n"
        "- Transfer to a wire rack, and let cool completely.\n"
    ),
    "Project Plan": (
        "| Task            | Jan | Feb | Mar | Apr | May | Jun |\n"
        "|-----------------|-----|-----|-----|-----|-----|-----|\n"
        "| Research        | ### | ### |     |     |     |     |\n"
        "| Design          |     | ### | ### |     |     |     |\n"
        "| Development     |     |     | ### | ### | ### |     |\n"
        "| Testing         |     |     |     |     | ### | ### |\n"
        "| Implementation  |     |     |     |     |     | ### |\n"
    ),
    "Grid Template": (
        "+--+--+--+--+--+\n"
        "|  |  |  |  |  |\n"
        "+--+--+--+--+--+\n"
        "|  |  |  |  |  |\n"
        "+--+--+--+--+--+\n"
        "|  |  |  |  |  |\n"
        "+--+--+--+--+--+\n"
        "|  |  |  |  |  |\n"
        "+--+--+--+--+--+\n"
    ),
    "Meeting Agenda": "Meeting Agenda:\n- Topic 1\n- Topic 2\n- Conclusion\n",
    "Business Letter": "Business Letter:\nDear [Name],\n\n[Body]\n\nSincerely,\n[Your Name]\n",
    "Shopping List": "Shopping List:\n- Item 1\n- Item 2\n- Item 3\n",
    "To-Do List": "To-Do List:\n- Task 1\n- Task 2\n- Task 3\n",
    "Event Invitation": "Event Invitation:\nYou are invited to [Event Name] on [Date] at [Location].\n",
}
