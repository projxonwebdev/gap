export default function Alum() {
  return (
    <div className="space-y-section-gap">
      <section className="space-y-12 bg-charcoal/30 p-8 md:p-12 rounded-xl border border-glass">
        <div className="flex flex-col md:flex-row justify-between md:items-end border-b border-glass pb-4 gap-4">
          <div className="space-y-2">
            <h2 className="font-headline-lg text-headline-lg text-on-surface">Alumni Syndicate</h2>
            <p className="font-body-md text-body-md text-slate-gray">Graduates of the GAP program leading global initiatives.</p>
          </div>
          <div className="flex gap-2">
            <select className="bg-charcoal border border-glass text-on-surface text-sm rounded px-3 py-2 outline-none">
              <option>All Cohorts</option>
              <option>Cohort 2023</option>
              <option>Cohort 2022</option>
            </select>
          </div>
        </div>
        
        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-8">
          {[1,2,3,4,5,6,7,8,9,10,11,12].map((i) => (
            <div key={i} className="text-center group cursor-pointer">
              <div className="w-24 h-24 mx-auto rounded-full bg-charcoal border border-glass mb-4 overflow-hidden relative grayscale group-hover:grayscale-0 transition-all duration-300">
                <div 
                  className="bg-cover bg-center w-full h-full opacity-60 group-hover:opacity-100 transition-opacity" 
                  style={{ backgroundImage: `url('https://i.pravatar.cc/300?img=${i + 30}')` }}
                ></div>
              </div>
              <h5 className="font-label-md text-on-surface group-hover:text-momentum-gold transition-colors">Example Alum {i}</h5>
              <p className="text-xs text-momentum-gold mt-1">Role {i}</p>
              <p className="text-xs text-slate-gray mt-1">Cohort '{20 + (i%4)}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Alumni Spotlights */}
      <section className="space-y-12">
        <div className="space-y-4">
          <h2 className="font-headline-lg text-3xl text-on-surface border-b border-glass pb-4">Alumni Spotlights</h2>
          <p className="text-slate-gray max-w-2xl">In-depth look at how GAP transformed their operational trajectory.</p>
        </div>
        
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {[1,2].map(i => (
            <div key={i} className="glass-card p-8 rounded-xl flex flex-col md:flex-row gap-6 items-start">
              <div className="w-24 h-24 shrink-0 rounded-full bg-charcoal border border-glass overflow-hidden">
                <div className="bg-cover bg-center w-full h-full grayscale" style={{ backgroundImage: `url('https://i.pravatar.cc/300?img=${i + 40}')` }}></div>
              </div>
              <div className="space-y-4">
                <h4 className="text-xl font-bold text-on-surface">Example Person {i}</h4>
                <p className="text-sm text-momentum-gold">Founder & CEO</p>
                <p className="text-slate-gray italic text-sm leading-relaxed">
                  "The strategic clarity I gained through the GAP cohort fundamentally changed how I operate. The advisors didn't just give answers; they engineered a framework for us to scale predictably from $10M to $50M ARR."
                </p>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
