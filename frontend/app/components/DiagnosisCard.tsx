"use client";

import { Diagnosis } from "../lib/codec";

interface Props {
  diagnosis: Diagnosis;
  avatarUrl?: string;
}

const CAT_LABEL: Record<string, string> = {
  souls_like:     "Souls-like",
  fps_competitivo:"FPS Comp.",
  hero_shooter:   "Hero Shooter",
  arpg:           "ARPG",
  battle_royale:  "Battle Royale",
  sandbox:        "Sandbox",
  survival:       "Survival",
  rpg:            "RPG",
  esporte:        "Esporte",
  roguelike:      "Roguelike",
  simulador:      "Simulador",
  visual_novel:   "Visual Novel",
  estrategia:     "Estratégia",
  horror:         "Horror",
  plataforma:     "Plataforma",
  mmo:            "MMO",
};

const CAT_COLOR: Record<string, { bg: string; border: string; text: string }> = {
  souls_like:      { bg: "rgba(220,38,38,0.1)",   border: "rgba(220,38,38,0.3)",   text: "#fca5a5" },
  fps_competitivo: { bg: "rgba(234,88,12,0.1)",   border: "rgba(234,88,12,0.3)",   text: "#fdba74" },
  hero_shooter:    { bg: "rgba(16,185,129,0.1)",  border: "rgba(16,185,129,0.3)",  text: "#6ee7b7" },
  arpg:            { bg: "rgba(217,119,6,0.1)",   border: "rgba(217,119,6,0.3)",   text: "#fcd34d" },
  battle_royale:   { bg: "rgba(239,68,68,0.1)",   border: "rgba(239,68,68,0.3)",   text: "#fca5a5" },
  sandbox:         { bg: "rgba(20,184,166,0.1)",  border: "rgba(20,184,166,0.3)",  text: "#99f6e4" },
  survival:        { bg: "rgba(34,197,94,0.1)",   border: "rgba(34,197,94,0.3)",   text: "#86efac" },
  rpg:             { bg: "rgba(139,92,246,0.1)",  border: "rgba(139,92,246,0.3)",  text: "#c4b5fd" },
  esporte:         { bg: "rgba(59,130,246,0.1)",  border: "rgba(59,130,246,0.3)",  text: "#93c5fd" },
  roguelike:       { bg: "rgba(236,72,153,0.1)",  border: "rgba(236,72,153,0.3)",  text: "#f9a8d4" },
  simulador:       { bg: "rgba(99,102,241,0.1)",  border: "rgba(99,102,241,0.3)",  text: "#a5b4fc" },
  visual_novel:    { bg: "rgba(244,114,182,0.1)", border: "rgba(244,114,182,0.3)", text: "#fbcfe8" },
  estrategia:      { bg: "rgba(245,158,11,0.1)",  border: "rgba(245,158,11,0.3)",  text: "#fde68a" },
  horror:          { bg: "rgba(120,53,15,0.15)",  border: "rgba(180,83,9,0.3)",    text: "#fbbf24" },
  plataforma:      { bg: "rgba(6,182,212,0.1)",   border: "rgba(6,182,212,0.3)",   text: "#67e8f9" },
  mmo:             { bg: "rgba(139,92,246,0.12)", border: "rgba(167,139,250,0.3)", text: "#ddd6fe" },
};

const DEFAULT_COLOR = { bg: "rgba(100,116,139,0.1)", border: "rgba(100,116,139,0.3)", text: "#94a3b8" };

export default function DiagnosisCard({ diagnosis, avatarUrl }: Props) {
  return (
    <div style={{
      width: "100%", maxWidth: "580px",
      background: "linear-gradient(160deg, rgba(13,18,28,0.99) 0%, rgba(8,12,20,0.99) 100%)",
      border: "1px solid rgba(255,70,85,0.22)",
      borderRadius: "20px",
      overflow: "hidden",
      boxShadow: "0 0 0 1px rgba(255,70,85,0.05), 0 40px 100px rgba(0,0,0,0.7), 0 0 60px rgba(255,70,85,0.06)",
    }}>

      {/* ── Title bar ── */}
      <div style={{
        padding: "0.875rem 1.375rem",
        background: "rgba(255,70,85,0.04)",
        borderBottom: "1px solid rgba(255,70,85,0.1)",
        display: "flex", alignItems: "center", justifyContent: "space-between",
      }}>
        <div style={{ display: "flex", gap: "0.45rem" }}>
          {(["#FF5F57","#FEBC2E","#28C840"] as const).map(c => (
            <div key={c} style={{ width: 11, height: 11, borderRadius: "50%", background: c, boxShadow: `0 0 5px ${c}80` }} />
          ))}
        </div>
        <span className="font-orbitron" style={{ fontSize: "0.56rem", letterSpacing: "0.22em", color: "#475569" }}>
          LAUDO CONFIDENCIAL — DR.K/GAMER
        </span>
        <span style={{ fontSize: "0.65rem", color: "rgba(100,116,139,0.3)", fontFamily: "monospace" }}>CID-2025</span>
      </div>

      {/* ── Red accent stripe ── */}
      <div style={{
        height: "2px",
        background: "linear-gradient(90deg, #FF4655 0%, rgba(139,92,246,0.8) 50%, transparent 100%)",
      }} />

      <div style={{ padding: "1.75rem" }}>

        {/* ── Patient header ── */}
        <div style={{
          display: "flex", alignItems: "center", gap: "1rem",
          marginBottom: "1.5rem",
          padding: "1rem 1.25rem",
          background: "rgba(255,255,255,0.02)",
          border: "1px solid rgba(255,255,255,0.04)",
          borderRadius: "12px",
        }}>
          {avatarUrl ? (
            <img
              src={avatarUrl}
              alt="avatar"
              style={{
                width: 56, height: 56, borderRadius: "12px",
                border: "2px solid rgba(255,70,85,0.4)",
                flexShrink: 0,
                boxShadow: "0 0 16px rgba(255,70,85,0.2)",
              }}
            />
          ) : (
            <div style={{
              width: 56, height: 56, borderRadius: "12px", flexShrink: 0,
              display: "flex", alignItems: "center", justifyContent: "center",
              background: "rgba(255,70,85,0.08)",
              border: "2px solid rgba(255,70,85,0.25)",
              fontSize: "1.4rem", fontWeight: 900, color: "#FF4655",
              fontFamily: "var(--font-orbitron), Orbitron, monospace",
              boxShadow: "0 0 16px rgba(255,70,85,0.15)",
            }}>
              {diagnosis.patient[0]?.toUpperCase() ?? "?"}
            </div>
          )}
          <div style={{ minWidth: 0 }}>
            <span className="font-orbitron" style={{ fontSize: "0.56rem", letterSpacing: "0.22em", color: "#475569", display: "block", marginBottom: "0.3rem" }}>
              PACIENTE
            </span>
            <p className="font-orbitron" style={{
              margin: 0, fontSize: "1.2rem", fontWeight: 700,
              color: "#fff", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis",
            }}>
              🛋️ {diagnosis.patient}
            </p>
          </div>
        </div>

        {/* ── CID ── */}
        <div style={{
          marginBottom: "1.25rem",
          padding: "1.1rem 1.25rem",
          background: "rgba(139,92,246,0.06)",
          border: "1px solid rgba(139,92,246,0.18)",
          borderRadius: "12px",
          position: "relative",
          overflow: "hidden",
        }}>
          {/* Purple left accent */}
          <div style={{
            position: "absolute", left: 0, top: 0, bottom: 0,
            width: "3px",
            background: "linear-gradient(180deg, #8B5CF6 0%, rgba(139,92,246,0.3) 100%)",
          }} />

          <span className="font-orbitron" style={{
            fontSize: "0.56rem", letterSpacing: "0.25em",
            color: "rgba(139,92,246,0.6)", display: "block", marginBottom: "0.5rem",
          }}>
            CID GAMER OFICIAL
          </span>
          <p className="font-orbitron" style={{
            margin: "0 0 0.75rem",
            fontSize: "0.9rem", fontWeight: 700, color: "#a78bfa", lineHeight: 1.45,
          }}>
            {diagnosis.cid}
          </p>
          {(diagnosis.dominant_categories?.length ?? 0) > 0 && (
            <div style={{ display: "flex", flexWrap: "wrap", gap: "0.35rem" }}>
              {diagnosis.dominant_categories.map(cat => {
                const c = CAT_COLOR[cat] ?? DEFAULT_COLOR;
                return (
                  <span key={cat} style={{
                    display: "inline-flex", padding: "0.2rem 0.65rem",
                    borderRadius: "99px", fontSize: "0.67rem",
                    background: c.bg, border: `1px solid ${c.border}`, color: c.text,
                    fontWeight: 500, letterSpacing: "0.02em",
                  }}>
                    {CAT_LABEL[cat] ?? cat}
                  </span>
                );
              })}
            </div>
          )}
        </div>

        {/* ── Symptoms ── */}
        <div style={{ marginBottom: "1.25rem" }}>
          <span className="font-orbitron" style={{
            fontSize: "0.56rem", letterSpacing: "0.22em",
            color: "#475569", display: "block", marginBottom: "0.6rem",
          }}>
            SINTOMAS OBSERVADOS
          </span>
          <div style={{ display: "flex", flexDirection: "column", gap: "0.2rem" }}>
            {diagnosis.symptoms.map((s, i) => (
              <div
                key={i}
                className="symptom-row"
                style={{
                  display: "flex", gap: "0.875rem", alignItems: "flex-start",
                  padding: "0.55rem 0.75rem 0.55rem 0.875rem",
                  borderRadius: "0 8px 8px 0",
                }}
              >
                <span className="font-orbitron" style={{
                  fontSize: "0.65rem", fontWeight: 700, color: "#FF4655",
                  flexShrink: 0, marginTop: "2px", opacity: 0.8,
                }}>
                  {String(i + 1).padStart(2, "0")}
                </span>
                <span style={{ fontSize: "0.875rem", color: "#cbd5e1", lineHeight: 1.55 }}>{s}</span>
              </div>
            ))}
          </div>
        </div>

        {/* ── Divider ── */}
        <div style={{ height: "1px", background: "rgba(255,70,85,0.07)", margin: "0 0 1.25rem" }} />

        {/* ── Prognosis ── */}
        <div style={{
          marginBottom: "1rem",
          padding: "1rem 1.25rem",
          background: "rgba(255,70,85,0.04)",
          border: "1px solid rgba(255,70,85,0.12)",
          borderRadius: "12px",
          position: "relative", overflow: "hidden",
        }}>
          <div style={{
            position: "absolute", left: 0, top: 0, bottom: 0, width: "3px",
            background: "linear-gradient(180deg, #FF4655 0%, rgba(255,70,85,0.3) 100%)",
          }} />
          <span className="font-orbitron" style={{ fontSize: "0.56rem", letterSpacing: "0.22em", color: "rgba(255,70,85,0.5)", display: "block", marginBottom: "0.4rem" }}>
            📊 PROGNÓSTICO
          </span>
          <p style={{ margin: 0, fontSize: "0.875rem", color: "#e2e8f0", lineHeight: 1.6, fontStyle: "italic" }}>
            {diagnosis.prognosis}
          </p>
        </div>

        {/* ── Remedy ── */}
        <div style={{
          padding: "1rem 1.25rem",
          background: "rgba(139,92,246,0.04)",
          border: "1px solid rgba(139,92,246,0.12)",
          borderRadius: "12px",
          position: "relative", overflow: "hidden",
        }}>
          <div style={{
            position: "absolute", left: 0, top: 0, bottom: 0, width: "3px",
            background: "linear-gradient(180deg, #8B5CF6 0%, rgba(139,92,246,0.3) 100%)",
          }} />
          <span className="font-orbitron" style={{ fontSize: "0.56rem", letterSpacing: "0.22em", color: "rgba(139,92,246,0.5)", display: "block", marginBottom: "0.4rem" }}>
            💊 REMÉDIO PRESCRITO
          </span>
          <p style={{ margin: 0, fontSize: "0.875rem", color: "#e2e8f0", lineHeight: 1.6 }}>
            {diagnosis.remedy}
          </p>
        </div>

        {/* ── Footer stamp ── */}
        <div style={{
          marginTop: "1.5rem",
          paddingTop: "1.25rem",
          borderTop: "1px solid rgba(255,255,255,0.04)",
          display: "flex", alignItems: "center", justifyContent: "space-between",
        }}>
          <span className="font-orbitron" style={{ fontSize: "0.58rem", letterSpacing: "0.08em", color: "rgba(100,116,139,0.35)" }}>
            DR. K. — SEM CRM
          </span>
          <span style={{ fontSize: "0.7rem", color: "rgba(100,116,139,0.2)" }}>
            🔁 COMPARTILHE COM O AMIGO QUE JOGA PIOR
          </span>
        </div>
      </div>
    </div>
  );
}
