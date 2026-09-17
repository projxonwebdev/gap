import re

with open('src/pages/Home.jsx', 'r') as f:
    content = f.read()

# Add Why GAP and Tech Stack before Our Vision
why_gap_and_tech_stack = """
{/* 5.5 Why Be In GAP */}
<section className="px-margin-mobile md:px-margin-desktop py-section-gap bg-charcoal border-y border-glass">
  <div className="max-w-container-max mx-auto text-center space-y-12">
    <div className="space-y-4">
      <h3 className="font-headline-lg text-headline-lg text-momentum-gold tracking-widest uppercase">Why Choose GAP?</h3>
      <p className="text-slate-gray max-w-2xl mx-auto font-body-md text-lg">GAP is not just a consulting group. It is an accelerator for your personal and professional evolution.</p>
    </div>
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
      <div className="space-y-4">
        <span className="material-symbols-outlined text-4xl text-momentum-gold">psychology</span>
        <h4 className="font-headline-lg text-xl text-on-surface">Personal Development</h4>
        <p className="text-slate-gray font-body-md">Push beyond your comfort zone with rigorous, personalized coaching that uncovers your true leadership potential.</p>
      </div>
      <div className="space-y-4">
        <span className="material-symbols-outlined text-4xl text-momentum-gold">model_training</span>
        <h4 className="font-headline-lg text-xl text-on-surface">Actionable Strategy</h4>
        <p className="text-slate-gray font-body-md">Move past theory and learn to execute real-world strategies that directly impact the bottom line.</p>
      </div>
      <div className="space-y-4">
        <span className="material-symbols-outlined text-4xl text-momentum-gold">network_node</span>
        <h4 className="font-headline-lg text-xl text-on-surface">Elite Network</h4>
        <p className="text-slate-gray font-body-md">Gain access to a closed-door community of top-tier professionals, mentors, and industry veterans.</p>
      </div>
      <div className="space-y-4">
        <span className="material-symbols-outlined text-4xl text-momentum-gold">trending_up</span>
        <h4 className="font-headline-lg text-xl text-on-surface">Career Velocity</h4>
        <p className="text-slate-gray font-body-md">GAP alumni consistently step into senior roles faster, equipped with the executive presence to succeed.</p>
      </div>
    </div>
  </div>
</section>

{/* 5.6 Tech Stack */}
<section className="px-margin-mobile md:px-margin-desktop py-section-gap bg-obsidian">
  <div className="max-w-container-max mx-auto text-center space-y-12">
    <h3 className="font-headline-lg text-headline-lg text-momentum-gold tracking-widest uppercase">Our Tech Stack</h3>
    <div className="flex flex-wrap justify-center items-center gap-12 md:gap-24 opacity-60">
      <div className="flex flex-col items-center gap-2">
        <span className="material-symbols-outlined text-5xl">rocket_launch</span>
        <span className="font-label-md tracking-widest uppercase text-xs">Antigravity</span>
      </div>
      <div className="flex flex-col items-center gap-2">
        <span className="material-symbols-outlined text-5xl">code</span>
        <span className="font-label-md tracking-widest uppercase text-xs">Cursor</span>
      </div>
      <div className="flex flex-col items-center gap-2">
        <span className="material-symbols-outlined text-5xl">deployed_code</span>
        <span className="font-label-md tracking-widest uppercase text-xs">GitHub</span>
      </div>
      <div className="flex flex-col items-center gap-2">
        <span className="material-symbols-outlined text-5xl">database</span>
        <span className="font-label-md tracking-widest uppercase text-xs">Supabase</span>
      </div>
    </div>
  </div>
</section>
"""

content = content.replace('{/* 6. Our Vision */}', why_gap_and_tech_stack + '\n{/* 6. Our Vision */}')

with open('src/pages/Home.jsx', 'w') as f:
    f.write(content)

print("Home.jsx updated.")
