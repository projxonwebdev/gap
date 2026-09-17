import { useState } from 'react';

const faqs = [
  {
    q: "How does GAP differ from MIP?",
    a: "MIP is the foundational internship program where operational skills are built. GAP is the elite advisory tier for top-performing MIP alumni to consult on high-stakes client projects."
  },
  {
    q: "How can my company hire GAP?",
    a: "You can submit a project request via the 'Work with GAP' form. We evaluate engagements based on our current capacity and the strategic alignment with our advisors."
  },
  {
    q: "What is the typical engagement cadence?",
    a: "We operate on strict 30, 60, and 90-day sprint cadences to ensure rapid delivery and clear milestones."
  }
];

export default function Contact() {
  const [openFaq, setOpenFaq] = useState(null);

  return (
    <div className="space-y-section-gap">
      
      {/* Banner */}
      <section className="w-full py-16 flex justify-center items-center rounded-xl">
        <div className="flex flex-col items-center opacity-70">
          <img src="/projxon-logo.png" alt="PROJXON" className="h-16 md:h-24 w-auto object-contain mix-blend-screen" onError={(e) => e.target.style.display='none'} />
        </div>
      </section>

      {/* Contact Info */}
      <section className="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-4xl mx-auto">
        <div className="glass-card p-8 rounded-xl text-center space-y-4 border-t-2 border-momentum-gold">
          <span className="material-symbols-outlined text-4xl text-momentum-gold">location_on</span>
          <h3 className="font-headline-lg text-xl text-on-surface">Vegas Office</h3>
          <p className="text-slate-gray font-body-md">
            201 Las Vegas Blvd S<br />
            Las Vegas, NV 89101
          </p>
        </div>
        <div className="glass-card p-8 rounded-xl text-center space-y-4 border-t-2 border-momentum-gold">
          <span className="material-symbols-outlined text-4xl text-momentum-gold">phone</span>
          <h3 className="font-headline-lg text-xl text-on-surface">Office Cell</h3>
          <p className="text-slate-gray font-body-md">
            725-256-2693
          </p>
        </div>
      </section>

      {/* FAQs */}
      <section className="max-w-3xl mx-auto space-y-8">
        <div className="text-center space-y-2 mb-12">
          <h2 className="font-headline-xl text-3xl md:text-4xl text-on-surface">Frequently Asked Questions</h2>
          <p className="text-slate-gray">Common inquiries regarding GAP engagements.</p>
        </div>

        <div className="space-y-4">
          {faqs.map((faq, idx) => (
            <div 
              key={idx} 
              className="glass-card border border-glass rounded-lg overflow-hidden transition-all duration-300"
            >
              <button 
                className="w-full p-6 text-left flex justify-between items-center hover:bg-surface-tint/5"
                onClick={() => setOpenFaq(openFaq === idx ? null : idx)}
              >
                <span className="font-body-lg font-semibold text-on-surface">{faq.q}</span>
                <span className={`material-symbols-outlined text-momentum-gold transition-transform duration-300 ${openFaq === idx ? 'rotate-180' : ''}`}>
                  expand_more
                </span>
              </button>
              
              <div 
                className={`px-6 text-slate-gray transition-all duration-300 overflow-hidden ${openFaq === idx ? 'pb-6 max-h-[200px] opacity-100' : 'max-h-0 opacity-0'}`}
              >
                {faq.a}
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
