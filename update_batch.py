import re

def update_layout():
    with open('src/components/Layout.jsx', 'r') as f:
        content = f.read()
    
    # Update app bar height
    content = content.replace('h-20 px-margin-desktop', 'h-24 px-margin-desktop')
    
    # Update logo size in navbar
    content = content.replace('className="h-10 w-auto object-contain mix-blend-screen"', 'className="h-16 md:h-20 w-auto object-contain mix-blend-screen"')
    
    # Update logo size in footer
    content = content.replace('className="h-10 w-auto object-contain mix-blend-screen opacity-80"', 'className="h-16 md:h-20 w-auto object-contain mix-blend-screen opacity-80"')
    
    with open('src/components/Layout.jsx', 'w') as f:
        f.write(content)

def update_home():
    with open('src/pages/Home.jsx', 'r') as f:
        content = f.read()
    
    # 3. Why choose gap section bg should be black like everywhere else.
    # From bg-charcoal to bg-obsidian
    content = content.replace('bg-charcoal border-y border-glass', 'bg-obsidian border-y border-glass')
    
    # 4. don't use shitty logos in why choose gap... use something else.
    # Replace material symbols with simple gold top borders on the cards instead
    content = content.replace('<span className="material-symbols-outlined text-4xl text-momentum-gold">psychology</span>', '')
    content = content.replace('<span className="material-symbols-outlined text-4xl text-momentum-gold">model_training</span>', '')
    content = content.replace('<span className="material-symbols-outlined text-4xl text-momentum-gold">network_node</span>', '')
    content = content.replace('<span className="material-symbols-outlined text-4xl text-momentum-gold">trending_up</span>', '')
    
    # Make the cards look better without logos by adding a border
    content = content.replace('<div className="space-y-4">', '<div className="space-y-4 border-t border-momentum-gold/40 pt-4">')
    
    # 5. Tech stack: use actual company logos (Cursor, Antigravity, GitHub, Vercel, AWS)
    tech_stack_html = """
    <div className="flex flex-wrap justify-center items-center gap-12 md:gap-24 opacity-80">
      <div className="flex flex-col items-center gap-3">
        <img src="https://cdn.simpleicons.org/github/e2e2e2" alt="GitHub" className="h-10 md:h-12 w-auto" />
        <span className="font-label-md tracking-widest uppercase text-xs text-slate-gray">GitHub</span>
      </div>
      <div className="flex flex-col items-center gap-3">
        <img src="https://cdn.simpleicons.org/vercel/e2e2e2" alt="Vercel" className="h-10 md:h-12 w-auto" />
        <span className="font-label-md tracking-widest uppercase text-xs text-slate-gray">Vercel</span>
      </div>
      <div className="flex flex-col items-center gap-3">
        <img src="https://cdn.simpleicons.org/amazonaws/e2e2e2" alt="AWS" className="h-10 md:h-12 w-auto" />
        <span className="font-label-md tracking-widest uppercase text-xs text-slate-gray">AWS</span>
      </div>
      <div className="flex flex-col items-center gap-3">
        <div className="h-10 md:h-12 flex items-center justify-center font-display-lg text-2xl font-bold text-[#e2e2e2]">AGY</div>
        <span className="font-label-md tracking-widest uppercase text-xs text-slate-gray">Antigravity</span>
      </div>
      <div className="flex flex-col items-center gap-3">
        <div className="h-10 md:h-12 flex items-center justify-center font-display-lg text-2xl font-bold text-[#e2e2e2]">|_</div>
        <span className="font-label-md tracking-widest uppercase text-xs text-slate-gray">Cursor</span>
      </div>
    </div>
"""
    # Replace the old tech stack grid with this one
    content = re.sub(r'<div className="flex flex-wrap justify-center items-center gap-12 md:gap-24 opacity-60">.*?</div>\n  </div>\n</section>', tech_stack_html + '  </div>\n</section>', content, flags=re.DOTALL)
    
    with open('src/pages/Home.jsx', 'w') as f:
        f.write(content)

def update_contact():
    with open('src/pages/Contact.jsx', 'r') as f:
        content = f.read()
    
    # 6. In contacts, dont fake address and phone number, just say coming soon
    content = content.replace("""
            123 PROJXON Plaza<br/>
            Innovation District<br/>
            Cityville, ST 12345
""", "\n            Coming Soon\n")
    content = content.replace("""
            +1 (555) 123-4567<br/>
            Mon-Fri, 9am - 6pm EST
""", "\n            Coming Soon\n")
    
    with open('src/pages/Contact.jsx', 'w') as f:
        f.write(content)

def update_mip():
    with open('src/pages/MIP.jsx', 'r') as f:
        content = f.read()
    
    # 8. write a little about MIP and fix Venn Diagram
    # I will replace the messy CSS venn diagram with a much sleeker 3-node graph layout
    new_mip_html = """export default function MIP() {
  return (
    <div className="space-y-section-gap">
      <section className="text-center max-w-4xl mx-auto space-y-6">
         <h1 className="font-headline-xl text-[40px] md:text-[56px] text-on-surface">The Management Internship Program <span className="text-momentum-gold">(MIP)</span></h1>
         <p className="text-slate-gray text-lg md:text-xl leading-relaxed">
           MIP is the foundational proving ground for all PROJXON leaders. Over the course of this rigorous program, 
           interns are trained in operational excellence, strategic thinking, and project execution. 
           It acts as the strict prerequisite gauntlet—ensuring that every single member of the Growth Advisory Program 
           enters with the exact same uncompromised baseline of professional competence and resilience.
         </p>
      </section>

      {/* Sleek Tri-Node Intersection Diagram */}
      <section className="w-full max-w-5xl mx-auto py-12 md:py-24 flex flex-col items-center">
        <h3 className="font-headline-lg text-2xl text-on-surface mb-16 uppercase tracking-widest border-b border-momentum-gold/30 pb-2">Where GAP Sits</h3>
        
        <div className="relative w-full flex flex-col md:flex-row items-center justify-center gap-12 md:gap-8">
          
          {/* Left Node: PROJXON */}
          <div className="flex flex-col items-center z-10 w-full md:w-1/3">
             <div className="w-32 h-32 rounded-2xl bg-surface-container border border-glass flex items-center justify-center shadow-lg p-6 mb-4">
                <img src="/projxon-logo.png" alt="PROJXON" className="w-full h-auto mix-blend-screen opacity-90" />
             </div>
             <h4 className="font-headline-lg text-lg text-momentum-gold uppercase tracking-widest">Internal Talent</h4>
             <p className="text-slate-gray text-center text-sm mt-2">The highest performing talent sourced directly from PROJXON.</p>
          </div>

          {/* Connection Lines (Desktop) */}
          <div className="hidden md:block absolute top-16 left-1/4 right-1/4 h-[2px] bg-gradient-to-r from-glass via-momentum-gold to-glass z-0"></div>

          {/* Center Hub: GAP */}
          <div className="flex flex-col items-center z-20 w-full md:w-1/3 relative transform md:-translate-y-8">
             <div className="absolute inset-0 bg-momentum-gold/20 blur-[60px] rounded-full pointer-events-none"></div>
             <div className="w-48 h-48 rounded-full bg-obsidian border-2 border-momentum-gold flex flex-col items-center justify-center shadow-[0_0_50px_rgba(212,175,55,0.2)] p-8 mb-4 relative z-10">
                <img src="/gap-logo.png" alt="GAP" className="w-full h-auto mix-blend-screen" />
             </div>
             <h4 className="font-headline-xl text-2xl text-on-surface font-semibold tracking-widest mt-2">The Intersection</h4>
          </div>

          {/* Right Node: Clients */}
          <div className="flex flex-col items-center z-10 w-full md:w-1/3">
             <div className="w-32 h-32 rounded-2xl bg-surface-container border border-glass flex items-center justify-center shadow-lg p-6 mb-4">
                <span className="material-symbols-outlined text-[60px] text-slate-gray">domain</span>
             </div>
             <h4 className="font-headline-lg text-lg text-momentum-gold uppercase tracking-widest">Portfolio Clients</h4>
             <p className="text-slate-gray text-center text-sm mt-2">External businesses requiring elite strategic advisory.</p>
          </div>

        </div>

        {/* Bottom Node: MIP (Feeds up into GAP) */}
        <div className="relative w-full flex flex-col items-center justify-center mt-12 md:-mt-8 z-10">
           {/* Vertical connection line */}
           <div className="hidden md:block absolute bottom-full left-1/2 w-[2px] h-16 bg-gradient-to-t from-glass to-momentum-gold -translate-x-1/2 mb-2"></div>
           
           <div className="flex flex-col items-center w-full md:w-1/3">
              <div className="w-32 h-32 rounded-2xl bg-surface-container border border-glass flex items-center justify-center shadow-lg p-6 mb-4">
                 <img src="/mip-logo.png" alt="MIP" className="w-full h-auto mix-blend-screen opacity-90" />
              </div>
              <h4 className="font-headline-lg text-lg text-momentum-gold uppercase tracking-widest">The Foundation</h4>
              <p className="text-slate-gray text-center text-sm mt-2">The operational prerequisite gauntlet.</p>
           </div>
        </div>

      </section>
    </div>
  );
}
"""
    with open('src/pages/MIP.jsx', 'w') as f:
        f.write(new_mip_html)

if __name__ == '__main__':
    update_layout()
    update_home()
    update_contact()
    update_mip()
    print("All files updated successfully.")
