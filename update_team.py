import re

with open('src/pages/Team.jsx', 'r') as f:
    content = f.read()

new_content = """export default function Team() {
  const currentMembers = [
    { name: "Zeba Ladiwala", role: "Program Lead" },
    { name: "Aishwarya Raj Soppadandi", role: "Sr. IT Analyst" },
    { name: "Simeon Davenport", role: "Sr. Web Developer" },
    { name: "Atharva", role: "Advisor" },
    { name: "Ram", role: "Advisor" },
    { name: "Sobhana", role: "Advisor" },
    { name: "Bast", role: "Advisor" },
  ];

  return (
    <div className="space-y-section-gap">
      <section className="space-y-12">
        <div className="space-y-4">
          <h2 className="font-headline-xl text-headline-xl text-on-surface border-b border-glass pb-4">Current Active Members</h2>
          <p className="text-slate-gray max-w-2xl">The dedicated leadership and advisors steering the vision of GAP.</p>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-gutter">
          {currentMembers.map((member, i) => (
            <div key={i} className="group cursor-pointer">
              <div className="aspect-[3/4] w-full mb-4 bg-surface-container-low rounded-lg overflow-hidden border border-glass relative flex items-center justify-center transition-all duration-500 hover:border-momentum-gold/40 hover:-translate-y-2 hover:shadow-[0_12px_40px_rgba(212,175,55,0.1)]">
                {/* Default no-person image (Material Icon) */}
                <span className="material-symbols-outlined text-[100px] text-slate-gray opacity-20 group-hover:opacity-40 group-hover:text-momentum-gold transition-all duration-500">
                  person
                </span>
                
                <div className="absolute inset-0 bg-gradient-to-t from-obsidian via-obsidian/40 to-transparent opacity-90"></div>
                
                <div className="absolute bottom-4 left-4 right-4">
                  <h4 className="font-body-lg text-body-lg font-semibold text-on-surface mb-1 group-hover:text-momentum-gold transition-colors">{member.name}</h4>
                  <p className="font-caption text-caption text-slate-gray uppercase tracking-widest">{member.role}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="bg-momentum-gold/10 border border-momentum-gold/30 p-12 rounded-xl text-center space-y-6">
        <h3 className="font-headline-lg text-3xl text-momentum-gold">Join the Advisory Network</h3>
        <p className="text-on-surface max-w-2xl mx-auto">We are always looking for seasoned executives to join our mentorship rotation.</p>
        <button className="bg-momentum-gold text-obsidian px-8 py-4 rounded font-bold hover:bg-white transition-colors">
            Apply to Advise
        </button>
      </section>
    </div>
  );
}
"""

with open('src/pages/Team.jsx', 'w') as f:
    f.write(new_content)

print("Merged successfully.")
