"""
    NFL MVP Tracker -- Main Driver
    Judah Ellison
    December 2023/January 2024
"""
# Import other files
import code_settings
import code_functions as f

# Main Driver
def main():
    code_settings.screen.onclick(f.print_coordinates)
    code_settings.turtle.done()

if __name__ == "__main__":
    main()
