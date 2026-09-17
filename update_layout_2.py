import re

with open('src/components/Layout.jsx', 'r') as f:
    content = f.read()

# Update Navbar
navbar_replacement = """            <Link to="/" className="cursor-pointer active:opacity-80 transition-opacity duration-300">
              <img src="/gap-logo.png" alt="GAP" className="h-16 md:h-20 w-auto object-contain mix-blend-screen" />
            </Link>
            <div className="flex items-center gap-8">
              <div className="hidden md:flex gap-gutter items-center tracking-widest">
                <Link to="/" className="text-on-surface-variant hover:text-momentum-gold-bright transition-colors duration-300 font-label-md text-label-md cursor-pointer active:opacity-80">Home</Link>
                <Link to="/portfolio" className="text-on-surface-variant hover:text-momentum-gold-bright transition-colors duration-300 font-label-md text-label-md cursor-pointer active:opacity-80">Portfolio</Link>
                <Link to="/team" className="text-on-surface-variant hover:text-momentum-gold-bright transition-colors duration-300 font-label-md text-label-md cursor-pointer active:opacity-80">Team</Link>
                <Link to="/mip" className="text-on-surface-variant hover:text-momentum-gold-bright transition-colors duration-300 font-label-md text-label-md cursor-pointer active:opacity-80">MIP</Link>
                <Link to="/coaching" className="text-on-surface-variant hover:text-momentum-gold-bright transition-colors duration-300 font-label-md text-label-md cursor-pointer active:opacity-80">Coaching</Link>
              </div>
              <Link to="/work" className="font-label-md text-label-md text-obsidian bg-momentum-gold px-4 md:px-8 py-2 rounded uppercase tracking-widest hover:scale-105 hover:shadow-[0_0_20px_rgba(212,175,55,0.4)] transition-all active:scale-95 hidden sm:flex justify-center items-center font-bold">
                Work with GAP
              </Link>
            </div>"""

content = re.sub(
    r'<Link to="/" className="cursor-pointer active:opacity-80 transition-opacity duration-300">.*?Work with GAP\n            </Link>', 
    navbar_replacement, 
    content, 
    flags=re.DOTALL
)

# Update Footer
footer_replacement = """        <footer className="bg-obsidian w-full border-t border-glass flat no shadows mt-auto relative">
          <div className="flex flex-col md:flex-row justify-between items-center py-unit px-margin-desktop max-w-container-max mx-auto min-h-[80px]">
            <div className="mb-4 md:mb-0 flex flex-row items-center justify-center md:justify-start gap-3 w-full md:w-1/3">
              <img src="/gap-logo.png" alt="GAP" className="h-16 md:h-20 w-auto object-contain mix-blend-screen opacity-80" />
              <span className="font-label-md text-[10px] text-slate-gray tracking-[0.2em] uppercase mt-1">Powered by PROJXON</span>
            </div>
            <div className="font-caption text-caption text-slate-gray mb-4 md:mb-0 w-full md:w-1/3 flex justify-center text-center">
                © 2026 PROJXON. All rights reserved.
            </div>
            <div className="flex gap-6 w-full md:w-1/3 justify-center md:justify-end">
              <Link to="/contact" className="font-caption text-caption text-slate-gray hover:text-momentum-gold transition-colors duration-200 cursor-pointer">Contact</Link>
            </div>
          </div>
        </footer>"""

content = re.sub(
    r'<footer className="bg-obsidian w-full border-t border-glass flat no shadows mt-auto">.*?</footer>',
    footer_replacement,
    content,
    flags=re.DOTALL
)

with open('src/components/Layout.jsx', 'w') as f:
    f.write(content)

print("Layout updated.")
