# Author: Yoshi Jaeger
# License: MIT
# Tested with Sublime Text 4

import sublime
import sublime_plugin
import re

class SplitImportCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Only perform the action on selected text
        for region in self.view.sel():
            if not region.empty():
                # Extract the selected text
                selected_text = self.view.substr(region)
              
                # Split the tokens from the selected text and format it
                formatted_text = self.split_imports(selected_text)
              
                # Replace the selected text with the formatted text
                if formatted_text:
                    self.view.replace(edit, region, formatted_text)

    def split_imports(self, text):
        # Regular expression to match the import statement
        # ToDo: extensive testing, not sure if it works for every use case yet :(
        pattern = r"import\s+{([^}]+)}\s+from\s+['\"]([^'\"]+)['\"]"
        match = re.search(pattern, text)
        if match:
            items_string = match.group(1)
            from_part = match.group(2)
            items = items_string.split(',')

            # Clean up items and ensure they are unique
            cleaned_items = [item.strip() for item in items if item.strip()]
          
            # Ensure last item has a comma (airbnb style?)
            if cleaned_items[-1][-1] != ',':
                cleaned_items[-1] = cleaned_items[-1] + ','

            # Indention
            indent = ''
            tab_size = 2 # ToDo: make sure to read this from the currently opened file
            inner_indent = indent + ' ' * tab_size

            # Create the new formatted import statement
            new_import = (f"import {{\n{inner_indent}" + 
                          f",\n{inner_indent}".join(cleaned_items) + 
                          f"\n{indent}}}" + f" from '{from_part}';")

            return new_import
        return None
