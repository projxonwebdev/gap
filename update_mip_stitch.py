import re

new_mip_content = """export default function MIP() {
  return (
    <div className="space-y-section-gap">
      <section className="text-center max-w-4xl mx-auto space-y-6 flex flex-col items-center">
         <img src="/mip-logo.png" alt="MIP Logo" className="h-24 md:h-32 mb-4 object-contain mix-blend-screen opacity-90" />
         <h1 className="font-headline-xl text-[40px] md:text-[56px] text-on-surface">The Momentum Internship Program <span className="text-momentum-gold">(MIP)</span></h1>
         <p className="text-slate-gray text-lg md:text-xl leading-relaxed">
           MIP is the foundational proving ground for all PROJXON leaders. Over the course of this rigorous program, 
           interns are trained in operational excellence, strategic thinking, and project execution. 
           It acts as the strict prerequisite gauntlet—ensuring that every single member of the Growth Advisory Program 
           enters with the exact same uncompromised baseline of professional competence and resilience.
         </p>
      </section>

      {/* Venn Diagram Section from Stitch */}
      <section className="w-full max-w-5xl mx-auto py-12 md:py-24 flex flex-col items-center relative overflow-hidden">
        {/* Background Glow */}
        <div className="absolute inset-0 z-0 flex items-center justify-center opacity-20 pointer-events-none">
          <div className="w-[800px] h-[800px] bg-momentum-gold rounded-full blur-[150px]"></div>
        </div>
        
        <div className="text-center z-10 mb-20">
          <h1 className="font-display-lg text-display-lg text-momentum-gold-bright mb-4 tracking-widest uppercase text-3xl">The Nexus of Growth</h1>
        </div>

        {/* Venn Diagram Visualization */}
        <div className="relative w-full max-w-[600px] aspect-square z-10 transform scale-75 md:scale-100">
          {/* Top Left Circle: PROJXON */}
          <div className="absolute top-0 left-0 md:left-[50px] w-[250px] md:w-[350px] h-[250px] md:h-[350px] rounded-full border border-momentum-gold/30 bg-charcoal/40 backdrop-blur-xl flex flex-col items-center justify-start pt-12 md:pt-20 mix-blend-plus-lighter shadow-[0_0_30px_rgba(212,175,55,0.1)]">
            <img src="/projxon-logo.png" alt="PROJXON" className="w-16 md:w-24 mb-2 mix-blend-screen opacity-90 drop-shadow-[0_0_8px_rgba(255,215,0,0.5)]" />
            <span className="font-headline-lg text-sm md:text-xl text-on-surface tracking-wider drop-shadow-[0_0_8px_rgba(255,215,0,0.5)]">PROJXON</span>
          </div>

          {/* Top Right Circle: Portfolio Clients */}
          <div className="absolute top-0 right-0 md:right-[50px] w-[250px] md:w-[350px] h-[250px] md:h-[350px] rounded-full border border-momentum-gold/30 bg-charcoal/40 backdrop-blur-xl flex flex-col items-center justify-start pt-12 md:pt-20 mix-blend-plus-lighter shadow-[0_0_30px_rgba(212,175,55,0.1)]">
            <span className="material-symbols-outlined text-[40px] md:text-[60px] text-slate-gray mb-2 drop-shadow-[0_0_8px_rgba(255,215,0,0.5)]">domain</span>
            <span className="font-headline-lg text-sm md:text-xl text-on-surface tracking-wider text-center drop-shadow-[0_0_8px_rgba(255,215,0,0.5)]">Portfolio<br/>Clients</span>
          </div>

          {/* Bottom Center Circle: MIP */}
          <div className="absolute bottom-0 md:bottom-[50px] left-1/2 -translate-x-1/2 w-[250px] md:w-[350px] h-[250px] md:h-[350px] rounded-full border border-momentum-gold/30 bg-charcoal/40 backdrop-blur-xl flex flex-col items-center justify-end pb-12 md:pb-20 mix-blend-plus-lighter shadow-[0_0_30px_rgba(212,175,55,0.1)]">
            <img src="/mip-logo.png" alt="MIP" className="w-16 md:w-24 mb-2 mix-blend-screen opacity-90 drop-shadow-[0_0_8px_rgba(255,215,0,0.5)]" />
            <span className="font-headline-lg text-sm md:text-xl text-on-surface tracking-wider drop-shadow-[0_0_8px_rgba(255,215,0,0.5)]">MIP</span>
          </div>

          {/* Absolute Center Intersection: GAP */}
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 md:-translate-y-1/4 z-20 text-center flex flex-col items-center justify-center">
            <img src="/gap-logo.png" alt="GAP" className="w-16 md:w-28 mb-2 mix-blend-screen drop-shadow-[0_0_15px_rgba(255,215,0,0.8)]" />
          </div>
        </div>
      </section>

      {/* Why Join GAP */}
      <section className="px-margin-mobile md:px-margin-desktop py-section-gap bg-obsidian border-y border-glass">
        <div className="max-w-container-max mx-auto text-center space-y-12">
          <div className="space-y-4">
            <h3 className="font-headline-lg text-headline-lg text-momentum-gold tracking-widest uppercase">Why Join GAP?</h3>
            <p className="text-slate-gray max-w-2xl mx-auto font-body-md text-lg">GAP is not just a consulting group. It is an accelerator for your personal and professional evolution.</p>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            <div className="space-y-4 border-t border-momentum-gold/40 pt-4">
              <h4 className="font-headline-lg text-xl text-on-surface">Personal Development</h4>
              <p className="text-slate-gray font-body-md">Push beyond your comfort zone with rigorous, personalized coaching that uncovers your true leadership potential.</p>
            </div>
            <div className="space-y-4 border-t border-momentum-gold/40 pt-4">
              <h4 className="font-headline-lg text-xl text-on-surface">Actionable Strategy</h4>
              <p className="text-slate-gray font-body-md">Move past theory and learn to execute real-world strategies that directly impact the bottom line.</p>
            </div>
            <div className="space-y-4 border-t border-momentum-gold/40 pt-4">
              <h4 className="font-headline-lg text-xl text-on-surface">Elite Network</h4>
              <p className="text-slate-gray font-body-md">Gain access to a closed-door community of top-tier professionals, mentors, and industry veterans.</p>
            </div>
            <div className="space-y-4 border-t border-momentum-gold/40 pt-4">
              <h4 className="font-headline-lg text-xl text-on-surface">Career Velocity</h4>
              <p className="text-slate-gray font-body-md">GAP alumni consistently step into senior roles faster, equipped with the executive presence to succeed.</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
"""

with open('src/pages/MIP.jsx', 'w') as f:
    f.write(new_mip_content)

print("MIP.jsx updated.")
