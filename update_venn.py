import re

with open('src/pages/MIP.jsx', 'r') as f:
    content = f.read()

new_venn = """      {/* SVG Venn Diagram Section */}
      <section className="w-full mx-auto py-12 flex flex-col items-center relative overflow-hidden">
        <div className="text-center z-10 mb-8">
          <h1 className="font-display-lg text-display-lg text-momentum-gold-bright tracking-widest uppercase text-2xl md:text-3xl">The Nexus of Growth</h1>
        </div>

        {/* Perfect Mathematical SVG Venn Diagram - Clean & Large */}
        <div className="relative w-full max-w-[900px] aspect-square z-10 flex items-center justify-center p-4">
          <svg viewBox="0 0 600 600" className="w-full h-full">
            <defs>
              <linearGradient id="glassGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stopColor="rgba(255,255,255,0.03)" />
                <stop offset="100%" stopColor="rgba(212,175,55,0.08)" />
              </linearGradient>
            </defs>

            {/* Top Left Circle: PROJXON */}
            <circle cx="240" cy="231" r="210" fill="url(#glassGrad)" stroke="#D4AF37" strokeWidth="2" strokeOpacity="0.6" className="mix-blend-screen" />
            
            {/* Top Right Circle: Portfolio Clients */}
            <circle cx="360" cy="231" r="210" fill="url(#glassGrad)" stroke="#D4AF37" strokeWidth="2" strokeOpacity="0.6" className="mix-blend-screen" />
            
            {/* Bottom Circle: MIP */}
            <circle cx="300" cy="335" r="210" fill="url(#glassGrad)" stroke="#D4AF37" strokeWidth="2" strokeOpacity="0.6" className="mix-blend-screen" />

            {/* Labels and Logos */}
            
            {/* PROJXON Logo (Top Left) */}
            <g transform="translate(130, 110)">
              <image href="/projxon-logo.png" width="100" height="100" className="mix-blend-screen opacity-90" />
              <text x="50" y="120" fontFamily="Inter" fontSize="16" fontWeight="600" fill="#e5e2e1" textAnchor="middle" letterSpacing="0.1em">PROJXON</text>
            </g>

            {/* Portfolio Clients Text (Top Right) */}
            <g transform="translate(470, 150)">
              <text x="0" y="0" fontFamily="Manrope" fontSize="26" fontWeight="700" fill="#e5e2e1" textAnchor="middle">Portfolio</text>
              <text x="0" y="32" fontFamily="Manrope" fontSize="26" fontWeight="700" fill="#e5e2e1" textAnchor="middle">Clients</text>
            </g>

            {/* MIP Logo (Bottom) */}
            <g transform="translate(300, 450)">
              <image href="/mip-logo.png" x="-50" y="-60" width="100" height="100" className="mix-blend-screen opacity-90" />
              <text x="0" y="60" fontFamily="Inter" fontSize="16" fontWeight="600" fill="#e5e2e1" textAnchor="middle" letterSpacing="0.1em">MIP</text>
            </g>

            {/* GAP Logo (Absolute Center) */}
            <g transform="translate(300, 280)">
              <image href="/gap-logo.png" x="-100" y="-45" width="200" height="90" className="mix-blend-screen" />
            </g>

          </svg>
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

print("MIP updated.")
