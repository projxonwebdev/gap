import re

with open('src/pages/Home.jsx', 'r') as f:
    content = f.read()

start_idx = content.find('{/* 5. What You Get (Benefits Grid) */}')
end_idx = content.find('{/* 6. Our Vision */}')

card_class = "group bg-obsidian border border-glass p-8 rounded-xl transition-all duration-500 ease-out hover:-translate-y-2 hover:shadow-[0_12px_40px_rgba(212,175,55,0.15)] hover:border-momentum-gold/40 hover:bg-white/[0.02] flex flex-col h-full"
icon_class = "material-symbols-outlined text-momentum-gold text-[40px] mb-6 group-hover:scale-110 group-hover:text-momentum-gold-bright transition-transform duration-500 origin-left"
title_class = "font-headline-lg text-[22px] md:text-[24px] text-on-surface mb-3"
desc_class = "font-body-md text-slate-gray leading-relaxed flex-grow"

new_section = f"""{{/* 5. What You Get (Benefits Grid) */}}
<section className="px-margin-mobile md:px-margin-desktop py-section-gap bg-obsidian">
<div className="max-w-container-max mx-auto">
<h3 className="font-headline-lg text-headline-lg text-momentum-gold mb-16 tracking-widest uppercase text-center">What You Get</h3>
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
{{/* Feature 1 */}}
<div className="{card_class}">
<span className="{icon_class}">person</span>
<h4 className="{title_class}">Executive Presence & Leadership</h4>
<p className="{desc_class}">Develop your advisory voice and leadership identity through real interactions with C-suite and senior leaders.</p>
</div>
{{/* Feature 2 */}}
<div className="{card_class}">
<span className="{icon_class}">groups</span>
<h4 className="{title_class}">C-Suite Mentorship & Coaching</h4>
<p className="{desc_class}">Regular 1:1s and coaching sessions directly with PROJXON leadership — not templates, real mentorship.</p>
</div>
{{/* Feature 3 */}}
<div className="{card_class}">
<span className="{icon_class}">work</span>
<h4 className="{title_class}">Client Consulting Experience</h4>
<p className="{desc_class}">Contribute to and lead on real client deliverables that go into your portfolio and professional track record.</p>
</div>
{{/* Feature 4 */}}
<div className="{card_class}">
<span className="{icon_class}">trending_up</span>
<h4 className="{title_class}">Business Advisory Skills</h4>
<p className="{desc_class}">Sharpen your strategic thinking, problem-framing, and advisory communication skills across live projects.</p>
</div>
{{/* Feature 5 */}}
<div className="{card_class}">
<span className="{icon_class}">workspace_premium</span>
<h4 className="{title_class}">Personal Brand Building</h4>
<p className="{desc_class}">LinkedIn, portfolio, thought leadership — GAP actively supports your visibility as an emerging senior professional.</p>
</div>
{{/* Feature 6 */}}
<div className="{card_class}">
<span className="{icon_class}">hub</span>
<h4 className="{title_class}">Senior-Level Networking</h4>
<p className="{desc_class}">Build relationships with fellow advisors, GAP alumni, university partners, and industry professionals.</p>
</div>
</div>
</div>
</section>
"""

new_content = content[:start_idx] + new_section + content[end_idx:]

with open('src/pages/Home.jsx', 'w') as f:
    f.write(new_content)

print("Merged successfully.")
