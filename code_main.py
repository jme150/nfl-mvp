"""
    NFL MVP Tracker -- Main Driver
    Judah Ellison
    December 2023/January 2024
"""
# Import other files
import code_settings as s
import code_functions as f

# Main Driver
def main():
    f.draw_graph()
    s.screen.onclick(f.print_coordinates)
    s.turtle.done()

if __name__ == "__main__":
    main()
