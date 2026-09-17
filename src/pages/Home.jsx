import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="space-y-section-gap">
      {/* Hero Section */}
      <section className="relative w-screen left-1/2 -ml-[50vw] -mt-12 pt-12 min-h-[75vh] flex flex-col justify-center px-4 md:px-margin-desktop py-section-gap overflow-hidden">
        {/* Subtle abstract background element */}
        <div 
          className="absolute inset-0 z-0 opacity-20 pointer-events-none mix-blend-screen bg-cover bg-center" 
          style={{ backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuCIGLaEJvDYwvrCUPS86ofKJu0ionPDnuVJVrmB7Xb5bsySjEjmI7wGwuW1w_1bjMovx1UPCkSeQ8Q16WOxpb1NVhYGxfUgmO5UG4MJCLxjocGSTeVMnUpL1BlpfSjB41Mz2Kxuy_8QbCbAsuLGt8DU7KpvTeDomChDxtL1gAeATwxFtDmeTFdkQqBiN_8hnrc1b7wSSQCxyhVNXCPtgjGKkZLEabIvi9-5IlfJFtH9_FDsxYxdzqc_5H3yde1i1_kKVLUVuDuK-EM')" }}
        ></div>
        <div className="relative z-10 max-w-container-max mx-auto w-full mt-16 md:mt-24">
          <h1 className="font-display-lg text-5xl md:text-7xl leading-[1.1] tracking-tight text-on-surface font-black uppercase mb-8">
              Where Leaders<br/><span className="text-momentum-gold">Advise Leaders.</span>
          </h1>
          <p className="font-body-lg text-body-lg text-slate-gray mb-12 max-w-2xl md:text-xl">
              The premium advisory experience designed to give you the access, skills, and relationships that accelerate your career as a senior professional and advisor.
          </p>
          <div className="flex flex-col gap-4 w-full sm:w-auto sm:flex-row">
            <Link to="/work" className="w-full sm:w-auto bg-momentum-gold text-obsidian font-label-md text-label-md py-4 px-8 md:px-10 rounded flex justify-center items-center gap-2 hover:bg-momentum-gold-bright transition-colors shadow-[0_0_20px_rgba(212,175,55,0.15)] uppercase tracking-widest font-bold">
                Work with GAP
                <span className="material-symbols-outlined text-[18px]">arrow_forward</span>
            </Link>
            <button onClick={() => document.getElementById('welcome')?.scrollIntoView({ behavior: 'smooth' })} className="w-full sm:w-auto border border-glass text-on-surface font-label-md text-label-md py-4 px-8 md:px-10 rounded flex justify-center items-center hover:border-momentum-gold hover:text-momentum-gold transition-colors bg-charcoal/30 backdrop-blur-sm uppercase tracking-widest font-bold">
                Explore GAP
            </button>
            <a href="https://www.linkedin.com/company/growth-advisory-program-stem/about/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" className="w-[52px] h-[52px] shrink-0 bg-[#0a66c2] text-white rounded flex justify-center items-center hover:bg-[#004182] transition-colors shadow-[0_0_15px_rgba(10,102,194,0.2)] mx-auto sm:mx-0">
                <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
            </a>
          </div>
        </div>
      </section>

                  {/* Welcome & Mission Section */}
      <section id="welcome" className="px-margin-mobile md:px-margin-desktop py-section-gap bg-obsidian relative">
        {/* Gradient fade to smoothly blend the bottom of Section 1 into Section 2 */}
        <div className="absolute bottom-full left-0 w-full h-48 bg-gradient-to-b from-transparent to-obsidian pointer-events-none"></div>
        
        {/* Stitch Glassmorphic Welcome Card */}
        <div className="max-w-container-max mx-auto relative mb-section-gap">
          <div className="absolute -top-24 -left-24 w-64 h-64 bg-momentum-gold/5 rounded-full blur-[100px] pointer-events-none"></div>
          <div className="bg-surface-container-low/40 backdrop-blur-md border border-glass p-8 md:p-16 rounded-xl relative overflow-hidden">
            <div className="absolute top-0 left-0 w-1 h-full bg-momentum-gold"></div>
            
            <h3 className="font-headline-xl text-headline-xl md:text-[48px] md:leading-[56px] text-on-surface mb-8">
              Welcome to GAP
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
            <h3 className="font-headline-lg text-headline-lg text-momentum-gold mb-12 tracking-widest uppercase">GAP's Mission</h3>
            <blockquote className="w-full max-w-[1050px] mx-auto px-4 md:px-8">
              <p className="font-headline-xl text-[24px] md:text-[32px] leading-tight text-on-surface font-light italic [text-wrap:pretty]">
                "At PROJXON, mentorship is a dynamic partnership built on the informal exchange of knowledge, experience, and personal growth. GAP provides a flexible, thoughtful environment to explore your story, clarify your direction, and continue building both personally and professionally."
              </p>
            </blockquote>
            <div className="mt-12 h-[2px] w-24 bg-momentum-gold"></div>
          </div>
        </div>

      </section>

{/* 3. Comparison */}
<section className="px-margin-mobile md:px-margin-desktop py-section-gap bg-obsidian">
<div className="max-w-container-max mx-auto">
<div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
{/* Typical */}
<div className="bg-obsidian border border-glass p-8 rounded-xl opacity-70">
<h4 className="font-headline-lg text-headline-lg text-slate-gray mb-8 pb-4 border-b border-glass">Typical Alumni Programs</h4>
<ul className="space-y-6">
<li className="flex items-start gap-4 text-slate-gray">
<span className="material-symbols-outlined text-red-400 mt-1">close</span>
<div><strong className="text-on-surface">Executive Presence:</strong> Passive networking.</div>
</li>
<li className="flex items-start gap-4 text-slate-gray">
<span className="material-symbols-outlined text-red-400 mt-1">close</span>
<div><strong className="text-on-surface">C-Suite Mentorship:</strong> Rare or inaccessible.</div>
</li>
<li className="flex items-start gap-4 text-slate-gray">
<span className="material-symbols-outlined text-red-400 mt-1">close</span>
<div><strong className="text-on-surface">Client Access:</strong> None.</div>
</li>
<li className="flex items-start gap-4 text-slate-gray">
<span className="material-symbols-outlined text-red-400 mt-1">close</span>
<div><strong className="text-on-surface">Strategic Networking:</strong> Ad-hoc introductions.</div>
</li>
<li className="flex items-start gap-4 text-slate-gray">
<span className="material-symbols-outlined text-red-400 mt-1">close</span>
<div><strong className="text-on-surface">Accountability:</strong> Self-directed.</div>
</li>
</ul>
</div>
{/* GAP */}
<div className="bg-obsidian border border-momentum-gold/50 p-8 rounded-xl relative shadow-[0_0_30px_rgba(212,175,55,0.05)]">
<div className="absolute top-0 right-0 w-32 h-32 bg-momentum-gold/10 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none"></div>
<h4 className="font-headline-lg text-headline-lg text-momentum-gold mb-8 pb-4 border-b border-glass">Growth Advisory Program</h4>
<ul className="space-y-6">
<li className="flex items-start gap-4 text-slate-gray">
<span className="material-symbols-outlined text-momentum-gold mt-1">check</span>
<div><strong className="text-on-surface">Executive Presence:</strong> Curated development.</div>
</li>
<li className="flex items-start gap-4 text-slate-gray">
<span className="material-symbols-outlined text-momentum-gold mt-1">check</span>
<div><strong className="text-on-surface">C-Suite Mentorship:</strong> Direct, ongoing partnership.</div>
</li>
<li className="flex items-start gap-4 text-slate-gray">
<span className="material-symbols-outlined text-momentum-gold mt-1">check</span>
<div><strong className="text-on-surface">Client Access:</strong> Embedded advisory roles.</div>
</li>
<li className="flex items-start gap-4 text-slate-gray">
<span className="material-symbols-outlined text-momentum-gold mt-1">check</span>
<div><strong className="text-on-surface">Strategic Networking:</strong> Highly curated, intentional access.</div>
</li>
<li className="flex items-start gap-4 text-slate-gray">
<span className="material-symbols-outlined text-momentum-gold mt-1">check</span>
<div><strong className="text-on-surface">Accountability:</strong> Structured, measured growth.</div>
</li>
</ul>
</div>
</div>
</div>
</section>
{/* 4. Accelerating Talent (MIP) */}
<section className="px-margin-mobile md:px-margin-desktop py-section-gap bg-obsidian border-t border-glass">
  <div className="max-w-container-max mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-24 items-center">
    
    <div className="text-center flex flex-col items-center">
      <span className="font-label-md text-label-md text-momentum-gold tracking-widest uppercase mb-4 block">The Foundation</span>
      <h3 className="font-headline-xl text-headline-xl text-on-surface mb-8">Accelerating Talent (MIP)</h3>
      <p className="font-body-md text-body-md md:text-body-lg text-slate-gray max-w-xl mx-auto mb-12">
        The Management Internship Program (MIP) serves as the rigorous prerequisite foundation for all GAP participants, ensuring a shared baseline of operational excellence.
      </p>
      <div className="flex flex-col sm:flex-row justify-center gap-8 md:gap-24">
        <div className="text-center">
          <div className="text-[56px] font-display-lg text-momentum-gold font-extrabold mb-2">200+</div>
          <div className="font-label-md text-slate-gray uppercase tracking-wider">Interns Trained</div>
        </div>
        <div className="text-center">
          <div className="text-[56px] font-display-lg text-momentum-gold font-extrabold mb-2">14+</div>
          <div className="font-label-md text-slate-gray uppercase tracking-wider">Industries Served</div>
        </div>
      </div>
    </div>

    <div className="w-full relative">
      <div className="absolute -inset-4 bg-momentum-gold/5 blur-2xl rounded-full pointer-events-none"></div>
      <img 
        src="/group-photo.jpg" 
        alt="MIP Group Photo" 
        className="relative w-full aspect-[4/3] rounded-xl shadow-[0_0_30px_rgba(212,175,55,0.1)] border border-glass object-cover object-center z-10" 
      />
    </div>

  </div>
</section>
{/* 5. What You Get (Benefits Grid) */}
<section className="px-margin-mobile md:px-margin-desktop py-section-gap bg-obsidian">
<div className="max-w-container-max mx-auto">
<h3 className="font-headline-lg text-headline-lg text-momentum-gold mb-16 tracking-widest uppercase text-center">What You Get</h3>
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
{/* Feature 1 */}
<div className="group bg-obsidian border border-glass p-8 rounded-xl transition-all duration-500 ease-out hover:-translate-y-2 hover:shadow-[0_12px_40px_rgba(212,175,55,0.15)] hover:border-momentum-gold/40 hover:bg-white/[0.02] flex flex-col h-full">
<span className="material-symbols-outlined text-momentum-gold text-[40px] mb-6 group-hover:scale-110 group-hover:text-momentum-gold-bright transition-transform duration-500 origin-left">person</span>
<h4 className="font-headline-lg text-[22px] md:text-[24px] text-on-surface mb-3">Executive Presence & Leadership</h4>
<p className="font-body-md text-slate-gray leading-relaxed flex-grow">Develop your advisory voice and leadership identity through real interactions with C-suite and senior leaders.</p>
</div>
{/* Feature 2 */}
<div className="group bg-obsidian border border-glass p-8 rounded-xl transition-all duration-500 ease-out hover:-translate-y-2 hover:shadow-[0_12px_40px_rgba(212,175,55,0.15)] hover:border-momentum-gold/40 hover:bg-white/[0.02] flex flex-col h-full">
<span className="material-symbols-outlined text-momentum-gold text-[40px] mb-6 group-hover:scale-110 group-hover:text-momentum-gold-bright transition-transform duration-500 origin-left">groups</span>
<h4 className="font-headline-lg text-[22px] md:text-[24px] text-on-surface mb-3">C-Suite Mentorship & Coaching</h4>
<p className="font-body-md text-slate-gray leading-relaxed flex-grow">Regular 1:1s and coaching sessions directly with PROJXON leadership — not templates, real mentorship.</p>
</div>
{/* Feature 3 */}
<div className="group bg-obsidian border border-glass p-8 rounded-xl transition-all duration-500 ease-out hover:-translate-y-2 hover:shadow-[0_12px_40px_rgba(212,175,55,0.15)] hover:border-momentum-gold/40 hover:bg-white/[0.02] flex flex-col h-full">
<span className="material-symbols-outlined text-momentum-gold text-[40px] mb-6 group-hover:scale-110 group-hover:text-momentum-gold-bright transition-transform duration-500 origin-left">work</span>
<h4 className="font-headline-lg text-[22px] md:text-[24px] text-on-surface mb-3">Client Consulting Experience</h4>
<p className="font-body-md text-slate-gray leading-relaxed flex-grow">Contribute to and lead on real client deliverables that go into your portfolio and professional track record.</p>
</div>
{/* Feature 4 */}
<div className="group bg-obsidian border border-glass p-8 rounded-xl transition-all duration-500 ease-out hover:-translate-y-2 hover:shadow-[0_12px_40px_rgba(212,175,55,0.15)] hover:border-momentum-gold/40 hover:bg-white/[0.02] flex flex-col h-full">
<span className="material-symbols-outlined text-momentum-gold text-[40px] mb-6 group-hover:scale-110 group-hover:text-momentum-gold-bright transition-transform duration-500 origin-left">trending_up</span>
<h4 className="font-headline-lg text-[22px] md:text-[24px] text-on-surface mb-3">Business Advisory Skills</h4>
<p className="font-body-md text-slate-gray leading-relaxed flex-grow">Sharpen your strategic thinking, problem-framing, and advisory communication skills across live projects.</p>
</div>
{/* Feature 5 */}
<div className="group bg-obsidian border border-glass p-8 rounded-xl transition-all duration-500 ease-out hover:-translate-y-2 hover:shadow-[0_12px_40px_rgba(212,175,55,0.15)] hover:border-momentum-gold/40 hover:bg-white/[0.02] flex flex-col h-full">
<span className="material-symbols-outlined text-momentum-gold text-[40px] mb-6 group-hover:scale-110 group-hover:text-momentum-gold-bright transition-transform duration-500 origin-left">workspace_premium</span>
<h4 className="font-headline-lg text-[22px] md:text-[24px] text-on-surface mb-3">Personal Brand Building</h4>
<p className="font-body-md text-slate-gray leading-relaxed flex-grow">LinkedIn, portfolio, thought leadership — GAP actively supports your visibility as an emerging senior professional.</p>
</div>
{/* Feature 6 */}
<div className="group bg-obsidian border border-glass p-8 rounded-xl transition-all duration-500 ease-out hover:-translate-y-2 hover:shadow-[0_12px_40px_rgba(212,175,55,0.15)] hover:border-momentum-gold/40 hover:bg-white/[0.02] flex flex-col h-full">
<span className="material-symbols-outlined text-momentum-gold text-[40px] mb-6 group-hover:scale-110 group-hover:text-momentum-gold-bright transition-transform duration-500 origin-left">hub</span>
<h4 className="font-headline-lg text-[22px] md:text-[24px] text-on-surface mb-3">Senior-Level Networking</h4>
<p className="font-body-md text-slate-gray leading-relaxed flex-grow">Build relationships with fellow advisors, GAP alumni, university partners, and industry professionals.</p>
</div>
</div>
</div>
</section>

{/* 5.6 Tech Stack */}
<section className="px-margin-mobile md:px-margin-desktop py-section-gap bg-obsidian">
  <div className="max-w-container-max mx-auto text-center space-y-12">
    <h3 className="font-headline-lg text-headline-lg text-momentum-gold tracking-widest uppercase">Our Tech Stack</h3>
    
    
    <div className="flex flex-wrap justify-center items-center gap-16 md:gap-32 opacity-90 mt-8">
      <div className="flex flex-col items-center gap-4">
        <img src="/github-logo.svg" alt="GitHub" className="h-16 md:h-20 w-auto" />
        <span className="font-label-md tracking-widest uppercase text-sm md:text-base text-slate-gray">GitHub</span>
      </div>
      <div className="flex flex-col items-center gap-4">
        <img src="/vercel-logo.svg" alt="Vercel" className="h-14 md:h-16 w-auto" />
        <span className="font-label-md tracking-widest uppercase text-sm md:text-base text-slate-gray mt-2">Vercel</span>
      </div>
      <div className="flex flex-col items-center gap-4">
        <img src="/aws-color.png" alt="AWS" className="h-14 md:h-16 w-auto" />
        <span className="font-label-md tracking-widest uppercase text-sm md:text-base text-slate-gray mt-2">AWS</span>
      </div>
      <div className="flex flex-col items-center gap-4">
        <img src="/cursor-logo.png" alt="Cursor" className="h-16 md:h-20 w-auto mix-blend-screen opacity-90" />
        <span className="font-label-md tracking-widest uppercase text-sm md:text-base text-slate-gray">Cursor</span>
      </div>
      <div className="flex flex-col items-center gap-4">
        <img src="/google-antigravity-logo.png" alt="Antigravity" className="h-16 md:h-20 w-auto mix-blend-screen opacity-90" />
        <span className="font-label-md tracking-widest uppercase text-sm md:text-base text-slate-gray">Antigravity</span>
      </div>
    </div>
  </div>
</section>

{/* 6. Our Vision */}
<section className="px-margin-mobile md:px-margin-desktop py-section-gap bg-obsidian border-t border-glass">
  <div className="max-w-container-max mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-24 items-center">
    
    <div className="text-left flex flex-col justify-center">
      <h3 className="font-headline-lg text-headline-lg text-momentum-gold mb-12 tracking-widest uppercase">Our Vision</h3>
      <div className="font-headline-xl text-[18px] md:text-[20px] leading-relaxed text-on-surface mb-12 font-light italic space-y-6">
        <p>"At PROJXON our passion is for developing people, and our obsession is with perfecting that process.</p>
        <p>We created the Growth Advisory Program to give our most dedicated alumni a place to continue growing not by going back to school or starting over, but by stepping into the room where decisions are made.</p>
        <p>In GAP you will find more value in advising, mentoring, and consulting alongside us than in any traditional alumni program. Your growth is ongoing. Our commitment to you does not end at graduation."</p>
      </div>
      <div>
        <div className="font-headline-lg text-xl md:text-2xl text-momentum-gold mb-1">Mark W. "Phelan"</div>
        <div className="font-label-md text-slate-gray tracking-widest uppercase">CEO + Co-Founder @ PROJXON</div>
      </div>
    </div>

    <div className="w-full relative flex justify-center lg:justify-end">
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[110%] h-[110%] max-w-lg bg-momentum-gold/5 blur-[80px] rounded-full pointer-events-none"></div>
      <img 
        src="/headshot.jpg" 
        alt="Mark W. Phelan, CEO PROJXON" 
        className="relative w-full max-w-md aspect-square rounded-xl shadow-[0_0_20px_rgba(212,175,55,0.05)] border border-glass object-cover object-center z-10" 
      />
    </div>

  </div>
</section>

    </div>
  );
}
