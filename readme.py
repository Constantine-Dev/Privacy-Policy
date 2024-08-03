import markdown

async def ReadMe():
  with open('policy.md', 'r', encoding='utf-8') as f:
    html_content = markdown.markdown(f.read())
  return html_content