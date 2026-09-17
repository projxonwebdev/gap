import React from 'react';

export default function MIP() {
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

      {/* Venn Diagram Section from Image */}
      <section className="w-full mx-auto py-12 flex flex-col items-center relative overflow-hidden">
        <div className="text-center z-10 mb-8">
          <h1 className="font-display-lg text-display-lg text-momentum-gold-bright tracking-widest uppercase text-2xl md:text-3xl">The Nexus of Growth</h1>
        </div>

        <div className="relative w-full max-w-[900px] z-10 flex items-center justify-center p-4">
          <img src="/venn-new.png" alt="GAP Venn Diagram" className="w-full h-auto object-contain mix-blend-screen" />
        </div>
      </section>

      {/* Why Join GAP */}
      <section className="px-margin-mobile md:px-margin-desktop py-section-gap">
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

      {/* Join GAP Section */}
      <section className="max-w-3xl mx-auto text-center space-y-4 pt-12 mt-12">
        <h2 className="font-headline-xl text-3xl md:text-4xl text-on-surface">Join GAP</h2>
        <p className="text-slate-gray font-body-lg">
          Reach out to current GAP members to join the program after completing the MIP program first.
        </p>
      </section>
    </div>
  );
}
