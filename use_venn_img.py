import re

with open('src/pages/MIP.jsx', 'r') as f:
    content = f.read()

new_venn = """      {/* Venn Diagram Section from Image */}
      <section className="w-full mx-auto py-12 flex flex-col items-center relative overflow-hidden">
        <div className="text-center z-10 mb-8">
          <h1 className="font-display-lg text-display-lg text-momentum-gold-bright tracking-widest uppercase text-2xl md:text-3xl">The Nexus of Growth</h1>
        </div>

        <div className="relative w-full max-w-[900px] z-10 flex items-center justify-center p-4">
          <img src="/venn.png" alt="GAP Venn Diagram" className="w-full h-auto object-contain mix-blend-screen" />
        </div>
      </section>"""

content = re.sub(
    r'      {/\* SVG Venn Diagram Section \*/}.*?</section>',
    new_venn,
    content,
    flags=re.DOTALL
)

with open('src/pages/MIP.jsx', 'w') as f:
    f.write(content)

print("MIP updated with venn.png.")
