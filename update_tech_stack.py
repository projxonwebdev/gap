import re

with open('src/pages/Home.jsx', 'r') as f:
    content = f.read()

tech_stack_html = """
    <div className="flex flex-wrap justify-center items-center gap-12 md:gap-24 opacity-80">
      <div className="flex flex-col items-center gap-3">
        <img src="/github-logo.svg" alt="GitHub" className="h-10 md:h-12 w-auto" />
        <span className="font-label-md tracking-widest uppercase text-xs text-slate-gray">GitHub</span>
      </div>
      <div className="flex flex-col items-center gap-3">
        <img src="/vercel-logo.svg" alt="Vercel" className="h-8 md:h-10 w-auto" />
        <span className="font-label-md tracking-widest uppercase text-xs text-slate-gray mt-2">Vercel</span>
      </div>
      <div className="flex flex-col items-center gap-3">
        <img src="/aws-logo.svg" alt="AWS" className="h-8 md:h-10 w-auto" />
        <span className="font-label-md tracking-widest uppercase text-xs text-slate-gray mt-2">AWS</span>
      </div>
      <div className="flex flex-col items-center gap-3">
        <img src="/cursor-logo.svg" alt="Cursor" className="h-10 md:h-12 w-auto" />
        <span className="font-label-md tracking-widest uppercase text-xs text-slate-gray">Cursor</span>
      </div>
      <div className="flex flex-col items-center gap-3">
        <img src="/antigravity-logo.svg" alt="Antigravity" className="h-10 md:h-12 w-auto" />
        <span className="font-label-md tracking-widest uppercase text-xs text-slate-gray">Antigravity</span>
      </div>
    </div>
"""

content = re.sub(
    r'<div className="flex flex-wrap justify-center items-center gap-12 md:gap-24 opacity-80">.*?</div>\n  </div>\n</section>',
    tech_stack_html + '  </div>\n</section>',
    content,
    flags=re.DOTALL
)

with open('src/pages/Home.jsx', 'w') as f:
    f.write(content)

print("Home.jsx tech stack updated.")
