import re

with open('src/pages/Home.jsx', 'r') as f:
    content = f.read()

start_idx = content.find('{/* Welcome & Mission Section */}')
end_idx = content.find('{/* 3. Comparison */}')

new_section = """      {/* Welcome & Mission Section */}
      <section id="welcome" className="px-margin-mobile md:px-margin-desktop py-section-gap bg-obsidian relative">
        {/* Gradient fade to smoothly blend the bottom of Section 1 into Section 2 */}
        <div className="absolute bottom-full left-0 w-full h-48 bg-gradient-to-b from-transparent to-obsidian pointer-events-none"></div>
        
        {/* Stitch Glassmorphic Welcome Card */}
        <div className="max-w-container-max mx-auto relative mb-section-gap">
          <div className="absolute -top-24 -left-24 w-64 h-64 bg-momentum-gold/5 rounded-full blur-[100px] pointer-events-none"></div>
          <div className="bg-surface-container-low/40 backdrop-blur-md border border-glass p-8 md:p-16 rounded-xl relative overflow-hidden">
            <div className="absolute top-0 left-0 w-1 h-full bg-momentum-gold"></div>
            
            <h3 className="font-headline-xl text-headline-xl md:text-[48px] md:leading-[56px] text-on-surface mb-8 flex items-center justify-start gap-3 md:gap-4">
              Welcome to <img src="/GAP-logo-justgap.png" alt="GAP" className="h-10 md:h-14 w-auto object-contain mix-blend-screen" />
            </h3>
            
            <div className="grid md:grid-cols-2 gap-8 md:gap-16">
              <p className="font-body-md text-[18px] md:text-[20px] leading-relaxed text-slate-gray text-left">
                <span className="text-momentum-gold">PROJXON</span> is a veteran-owned professional development company headquartered in Las Vegas, NV. We build real-world programs that develop the next generation of strategic leaders through hands-on experience, mentorship, and access to the rooms where decisions are made.
              </p>
              <p className="font-body-md text-[18px] md:text-[20px] leading-relaxed text-slate-gray text-left">
                <span className="text-momentum-gold">The Growth Advisory Program (GAP)</span> is where our most dedicated MIP alumni return, not to start over, but to step up. As a GAP advisor, you are no longer a participant. You are a contributor, a mentor, and a leader in the PROJXON ecosystem.
              </p>
            </div>
          </div>
        </div>

        {/* Stitch Premium Mission Card */}
        <div className="max-w-container-max mx-auto relative">
          <div className="absolute inset-0 bg-momentum-gold/5 blur-[120px] rounded-full scale-75 pointer-events-none"></div>
          <div className="relative border-y border-glass py-16 md:py-24 flex flex-col items-center text-center">
            <span className="material-symbols-outlined text-momentum-gold text-[64px] mb-8 opacity-50">format_quote</span>
            <h3 className="font-headline-lg text-headline-lg text-on-surface mb-12 tracking-widest uppercase opacity-50">GAP's Mission</h3>
            <blockquote className="max-w-4xl">
              <p className="font-headline-xl text-[24px] md:text-[32px] leading-tight text-on-surface font-light italic">
                "At PROJXON, mentorship is a dynamic partnership built on the informal exchange of knowledge, experience, and personal growth. GAP provides a flexible, thoughtful environment to explore your story, clarify your direction, and continue building both personally and professionally."
              </p>
            </blockquote>
            <div className="mt-12 h-[2px] w-24 bg-momentum-gold"></div>
          </div>
        </div>

      </section>

"""

new_content = content[:start_idx] + new_section + content[end_idx:]

with open('src/pages/Home.jsx', 'w') as f:
    f.write(new_content)

print("Merged successfully.")
