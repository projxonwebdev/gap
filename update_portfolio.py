import os

content = """import React from 'react';

export default function Portfolio() {
  return (
    <div className="space-y-section-gap">
      <section className="space-y-4 text-center max-w-4xl mx-auto">
        <h2 className="font-headline-xl text-4xl md:text-5xl text-on-surface">Client Portfolio</h2>
        <p className="font-body-md text-lg text-slate-gray">
          High-impact initiatives driving growth and operational excellence across our client network.
        </p>
      </section>

      <section className="space-y-12 max-w-5xl mx-auto">
        {/* Celyfos Project */}
        <div className="glass-card p-8 md:p-10 rounded-xl border-t-4 border-t-momentum-gold flex flex-col md:flex-row gap-8 shadow-2xl bg-charcoal/40 backdrop-blur-md relative overflow-hidden">
          
          {/* Subtle glow effect behind the card */}
          <div className="absolute top-0 right-0 -mr-20 -mt-20 w-64 h-64 bg-momentum-gold/10 rounded-full blur-3xl pointer-events-none"></div>

          <div className="flex-1 space-y-6 relative z-10">
            <div>
              <div className="inline-block px-3 py-1 bg-momentum-gold/10 border border-momentum-gold/30 text-momentum-gold text-xs font-bold uppercase tracking-widest rounded-full mb-4">
                In Progress
              </div>
              <h3 className="font-headline-lg text-2xl md:text-3xl text-on-surface mb-2">
                CELYFOS®
              </h3>
              <p className="text-xl text-slate-gray font-body-md">
                Shopify Migration & E-Commerce Build
              </p>
            </div>
            
            <div className="space-y-4">
              <p className="text-on-surface-variant font-body-md leading-relaxed">
                <strong className="text-on-surface font-semibold">CELYFOS®</strong> is a handcrafted luxury leather goods brand based in Athens, Greece, founded by Andrew Vasilas — an aircraft engineer who applies precision engineering principles to every case he builds.
              </p>
              <p className="text-on-surface-variant font-body-md leading-relaxed">
                The GAP team is leading the full migration of Celyfos from Etsy to a custom Shopify storefront, handling everything from product architecture and navigation design to UI development and brand storytelling.
              </p>
            </div>

            <div className="space-y-4 pt-6 border-t border-glass">
              <h4 className="text-momentum-gold font-bold uppercase tracking-widest text-sm flex items-center gap-2">
                <span className="material-symbols-outlined text-lg">build</span>
                What We Built
              </h4>
              <ul className="text-slate-gray space-y-3 font-body-md">
                <li className="flex gap-3">
                  <span className="text-momentum-gold mt-1">•</span>
                  <span>Series-based navigation structure (RAW, ATLAS, SOFT) for the catalog.</span>
                </li>
                <li className="flex gap-3">
                  <span className="text-momentum-gold mt-1">•</span>
                  <span>Custom product pages with expandable tabs, collapsible specs, and brand storytelling sections.</span>
                </li>
                <li className="flex gap-3">
                  <span className="text-momentum-gold mt-1">•</span>
                  <span>Dedicated policy pages for Shipping, Returns & Guarantee, and Ordering & Shipping.</span>
                </li>
                <li className="flex gap-3">
                  <span className="text-momentum-gold mt-1">•</span>
                  <span>Redesigned header and footer matching the premium leather goods aesthetic.</span>
                </li>
                <li className="flex gap-3">
                  <span className="text-momentum-gold mt-1">•</span>
                  <span>Full product mapping — consolidating 80+ Etsy listings into 11 core catalog products.</span>
                </li>
              </ul>
            </div>

            <div className="pt-6 mt-6 border-t border-glass flex flex-col md:flex-row gap-6 justify-between">
              <div>
                <span className="text-slate-gray block mb-2 text-xs uppercase tracking-wider font-bold">GAP Team</span>
                <span className="text-on-surface font-body-md block">Zeba Ladiwala (Program Lead)</span>
                <span className="text-on-surface font-body-md block">Simeon Davenport (Web Developer)</span>
              </div>
              <div>
                <span className="text-slate-gray block mb-2 text-xs uppercase tracking-wider font-bold">Status</span>
                <span className="text-momentum-gold font-body-md block">Final polish and client handoff underway.</span>
                <span className="text-on-surface-variant text-sm mt-1 block italic">Prepping for Friday Showcase feedback.</span>
              </div>
            </div>
          </div>
        </div>
      </section>
      
      {/* Future Initiatives */}
      <section className="bg-charcoal/30 border border-glass p-8 md:p-12 rounded-xl text-center space-y-6 max-w-4xl mx-auto">
        <h3 className="font-headline-lg text-3xl text-on-surface">Partner With Us</h3>
        <p className="text-slate-gray max-w-2xl mx-auto">
          We are currently evaluating new market vectors and client engagements for our next cohort.
        </p>
        <button className="border border-momentum-gold text-momentum-gold px-6 py-3 rounded font-label-md hover:bg-momentum-gold/10 transition-colors">
            Start a Project
        </button>
      </section>
    </div>
  );
}
"""

with open("src/pages/Portfolio.jsx", "w") as f:
    f.write(content)

print("Portfolio.jsx updated successfully.")
