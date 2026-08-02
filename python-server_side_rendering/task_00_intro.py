#!/usr/bin/python3
"""
    Module containing a simple templating program that generates
    personalized invitation files from a template and a list of objects
"""

PLACEHOLDERS = ("name", "event_title", "event_date", "event_location")


def generate_invitations(template, attendees):
    """Generate one output_X.txt invitation file per attendee"""

    # Checking the input types
    if not isinstance(template, str):
        print("Error: template must be a string, got "
              "{}".format(type(template).__name__))
        return
    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries, got "
              "{}".format(type(attendees).__name__))
        return
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: attendees must be a list of dictionaries, got "
                  "{} inside the list".format(type(attendee).__name__))
            return

    # Checking for empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Processing every attendee and writing its own output file
    for index, attendee in enumerate(attendees, start=1):
        content = template
        for placeholder in PLACEHOLDERS:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            content = content.replace("{" + placeholder + "}", str(value))

        filename = "output_{}.txt".format(index)
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
        except Exception as e:
            print("An error occurred while writing {}: {}".format(filename, e))
