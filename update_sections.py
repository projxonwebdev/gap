import re

with open('src/pages/Home.jsx', 'r') as f:
    text = f.read()

# Define the new combined section
new_section = """      {/* Welcome & Mission Section */}
      <section id="welcome" className="px-margin-mobile md:px-margin-desktop py-section-gap bg-obsidian relative">
        {/* Gradient fade to smoothly blend the bottom of Section 1 into Section 2 */}
        <div className="absolute bottom-full left-0 w-full h-48 bg-gradient-to-b from-transparent to-obsidian pointer-events-none"></div>
        <div className="max-w-container-max mx-auto relative z-10 flex flex-col gap-16 md:gap-24">
          
          <div className="text-left">
            <h3 className="font-headline-xl text-headline-xl md:text-[48px] md:leading-[56px] text-on-surface mb-8 flex items-center justify-start gap-3 md:gap-4">
              Welcome to <img src="/GAP-logo-justgap.png" alt="GAP" className="h-10 md:h-14 w-auto object-contain mix-blend-screen" />
            </h3>
            <p className="font-headline-xl text-[32px] leading-tight md:text-[40px] text-on-surface font-light text-left">
                    PROJXON is a veteran-owned professional development company... The Growth Advisory Program (GAP) is where our most dedicated MIP alumni return to continue their trajectory toward high-level leadership and executive impact.
            </p>
          </div>

          <div>
            <h3 className="font-headline-lg text-headline-lg text-momentum-gold mb-4 uppercase tracking-widest text-sm text-left">GAP's Mission</h3>
            <p className="font-headline-xl text-[32px] leading-tight md:text-[40px] text-on-surface font-light text-left">
                        "At PROJXON, mentorship is a dynamic partnership designed to accelerate executive growth and drive meaningful business outcomes."
            </p>
          </div>

        </div>
      </section>"""

# Replace the old Welcome and Mission sections
start_idx = text.find('{/* Welcome Section */}')
end_idx = text.find('</section>', text.find('{/* 2. GAP\'s Mission */}')) + 10

if start_idx != -1 and end_idx != -1:
    text = text[:start_idx] + new_section + text[end_idx:]
    with open('src/pages/Home.jsx', 'w') as f:
        f.write(text)
    print("Successfully replaced Welcome and Mission sections.")
else:
    print("Could not find sections to replace.")
