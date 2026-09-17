import { useState } from 'react';

export default function WorkWithGap() {
  const [submitted, setSubmitted] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    const formData = new FormData(e.target);
    formData.append("access_key", "7b685c2a-b7cc-4578-bbb2-a2020f658395");
    
    const object = Object.fromEntries(formData);
    const json = JSON.stringify(object);

    try {
      const response = await fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: json
      });
      
      const data = await response.json();
      
      if (data.success) {
        setSubmitted(true);
      } else {
        alert("Form Error: " + (data.message || "Something went wrong."));
      }
    } catch (error) {
      alert("Network error. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  };

  if (submitted) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh] text-center space-y-6">
        <span className="material-symbols-outlined text-6xl text-momentum-gold">check_circle</span>
        <h2 className="font-headline-xl text-3xl text-on-surface">Request Received</h2>
        <p className="text-slate-gray max-w-md">Your project request has been submitted to the GAP advisory board. We will review the parameters and reach out shortly.</p>
        <button onClick={() => setSubmitted(false)} className="mt-8 border border-glass text-slate-gray hover:text-momentum-gold hover:border-momentum-gold px-6 py-2 rounded transition-colors">
          Submit Another Request
        </button>
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto space-y-12">
      <div className="text-center space-y-4">
        <h1 className="font-headline-xl text-4xl md:text-5xl text-on-surface">Work with GAP</h1>
        <p className="text-slate-gray text-lg">Submit a Strategic Framework Request (SFR) to engage our advisory board.</p>
      </div>

      <form 
        onSubmit={handleSubmit}
        className="glass-card p-8 md:p-12 rounded-xl space-y-8 border-t-4 border-t-momentum-gold"
      >
        
        <div className="space-y-6">
          <h3 className="font-headline-lg text-xl text-momentum-gold border-b border-glass pb-2">Client Information</h3>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <label className="font-label-md text-xs tracking-widest uppercase text-slate-gray">Full Name</label>
              <input required type="text" name="name" className="w-full bg-surface-container border border-glass rounded p-3 text-on-surface focus:outline-none focus:border-momentum-gold transition-colors" placeholder="Jane Doe" />
            </div>
            <div className="space-y-2">
              <label className="font-label-md text-xs tracking-widest uppercase text-slate-gray">Work Email</label>
              <input required type="email" name="email" className="w-full bg-surface-container border border-glass rounded p-3 text-on-surface focus:outline-none focus:border-momentum-gold transition-colors" placeholder="jane@company.com" />
            </div>
          </div>
          
          <div className="space-y-2">
            <label className="font-label-md text-xs tracking-widest uppercase text-slate-gray">Company / Organization</label>
            <input required type="text" name="company" className="w-full bg-surface-container border border-glass rounded p-3 text-on-surface focus:outline-none focus:border-momentum-gold transition-colors" placeholder="Acme Corp" />
          </div>
        </div>

        <div className="space-y-6">
          <h3 className="font-headline-lg text-xl text-momentum-gold border-b border-glass pb-2">Engagement Parameters</h3>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <label className="font-label-md text-xs tracking-widest uppercase text-slate-gray">Project Type</label>
              <select required name="project_type" className="w-full bg-surface-container border border-glass rounded p-3 text-on-surface focus:outline-none focus:border-momentum-gold transition-colors appearance-none">
                <option value="" disabled selected>Select a category...</option>
                <option value="growth">Growth & Scaling Strategy</option>
                <option value="turnaround">Operational Turnaround</option>
                <option value="leadership">Executive Leadership Coaching</option>
                <option value="gmt">Go-To-Market Planning</option>
                <option value="other">Other (Specify in details)</option>
              </select>
            </div>
            <div className="space-y-2">
              <label className="font-label-md text-xs tracking-widest uppercase text-slate-gray">Cadence</label>
              <select required name="cadence" className="w-full bg-surface-container border border-glass rounded p-3 text-on-surface focus:outline-none focus:border-momentum-gold transition-colors appearance-none">
                <option value="" disabled selected>Select duration...</option>
                <option value="30">30-Day Sprint</option>
                <option value="60">60-Day Implementation</option>
                <option value="90">90-Day Full Transformation</option>
              </select>
            </div>
          </div>

          <div className="space-y-2">
            <label className="font-label-md text-xs tracking-widest uppercase text-slate-gray">Project Details (SFR)</label>
            <textarea required name="details" rows="5" className="w-full bg-surface-container border border-glass rounded p-3 text-on-surface focus:outline-none focus:border-momentum-gold transition-colors resize-none" placeholder="Describe the problem you are trying to solve..."></textarea>
          </div>
        </div>

        <button 
          type="submit" 
          disabled={isSubmitting}
          className="w-full bg-momentum-gold text-obsidian font-bold uppercase tracking-widest py-4 rounded hover:bg-white hover:shadow-[0_0_20px_rgba(212,175,55,0.4)] transition-all disabled:opacity-70 disabled:cursor-not-allowed"
        >
          {isSubmitting ? "Submitting..." : "Submit Request"}
        </button>
      </form>
    </div>
  );
}
