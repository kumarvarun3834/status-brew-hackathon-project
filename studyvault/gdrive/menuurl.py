def generate_menu_html(menu_data):
    html_output = "<div class='menu'>\n"
    for semester, subjects in menu_data.items():
        html_output += f"  <div class='semester'><a href='/{semester}/'><button>{semester}</button></a>\n"
        html_output += "    <div class='subjects'>\n"
        for subject, years in subjects.items():
            html_output += f"      <div class='subject'><a href='/{semester}/{subject}/'><button>{subject}</button></a>\n"
            html_output += "        <div class='years'>\n"
            for year in years:
                html_output += f"          <a href='/{semester}/{subject}/{year}/'><button>{year}</button></a>\n"
            html_output += "        </div>\n"
            html_output += "      </div>\n"
        html_output += "    </div>\n"
        html_output += "  </div>\n"
    html_output += "</div>"
    return html_output
