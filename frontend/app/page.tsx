"use client";

import { useState, useRef, useCallback } from "react";
import { useRouter } from "next/navigation";
import { encodeDiagnosis, Diagnosis } from "./lib/codec";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

type Step = "idle" | "loading_profile" | "loading_diagnosis" | "error";

const STATS = [
  { v: "16+",  l: "Categorias"  },
  { v: "∞",    l: "Diagnósticos"},
  { v: "0%",   l: "Precisão"    },
];

export default function HomePage() {
  const router    = useRouter();
  const abortRef  = useRef<AbortController | null>(null);
  const [input, setInput] = useState("");
  const [step,  setStep]  = useState<Step>("idle");
  const [error, setError] = useState("");

  const isLoading = step === "loading_profile" || step === "loading_diagnosis";

  const handleSubmit = useCallback(async (e: React.FormEvent) => {
    e.preventDefault();
    const value = input.trim();
    if (!value || isLoading) return;

    abortRef.current?.abort();
    const controller = new AbortController();
    abortRef.current = controller;

    setError("");
    setStep("loading_profile");

    try {
      const id = value
        .replace(/^https?:\/\/steamcommunity\.com\/(id|profiles)\//, "")
        .replace(/\/$/, "");

      const profileRes = await fetch(`${API_URL}/steam/${encodeURIComponent(id)}`, {
        signal: controller.signal,
      });

      if (!profileRes.ok) {
        let detail = "Perfil não encontrado. Verifique se o perfil é público.";
        try { detail = (await profileRes.json()).detail ?? detail; } catch { /* usa default */ }
        throw new Error(detail);
      }

      const profile = await profileRes.json();
      setStep("loading_diagnosis");

      const diagnoseRes = await fetch(`${API_URL}/diagnose`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: profile.username, games: profile.games }),
        signal: controller.signal,
      });

      if (!diagnoseRes.ok) throw new Error("Erro ao gerar diagnóstico. Tente novamente.");

      const diagnosis: Diagnosis = await diagnoseRes.json();
      router.push(`/resultado/${encodeDiagnosis(diagnosis)}`);
    } catch (err: unknown) {
      if (err instanceof Error && err.name === "AbortError") return;
      setError(err instanceof Error ? err.message : "Erro desconhecido.");
      setStep("error");
    }
  }, [input, isLoading, router]);

  return (
    <main style={{ minHeight: "100vh", background: "#060910", position: "relative", overflow: "hidden" }}>

      {/* ── Ambient background glows ── */}
      <div aria-hidden style={{ position: "fixed", inset: 0, pointerEvents: "none", zIndex: 0 }}>
        {/* Top red glow */}
        <div style={{
          position: "absolute", top: "-20%", left: "50%", transform: "translateX(-50%)",
          width: "900px", height: "600px",
          background: "radial-gradient(ellipse, rgba(255,70,85,0.12) 0%, transparent 65%)",
          filter: "blur(1px)",
        }} />
        {/* Bottom purple glow */}
        <div style={{
          position: "absolute", bottom: "-10%", right: "-10%",
          width: "600px", height: "600px",
          background: "radial-gradient(ellipse, rgba(139,92,246,0.08) 0%, transparent 60%)",
        }} />
        {/* Grid */}
        <div className="bg-grid" style={{ position: "absolute", inset: 0, opacity: 0.5 }} />
      </div>

      {/* ── HEADER ── */}
      <header className="fade-up" style={{ position: "relative", zIndex: 1, textAlign: "center", paddingTop: "4rem", paddingBottom: "0.5rem" }}>
        {/* Badge */}
        <div style={{
          display: "inline-flex", alignItems: "center", gap: "0.4rem",
          padding: "0.3rem 0.9rem", borderRadius: "99px",
          background: "rgba(255,70,85,0.08)", border: "1px solid rgba(255,70,85,0.2)",
          marginBottom: "1.5rem",
        }}>
          <span style={{ width: 6, height: 6, borderRadius: "50%", background: "#FF4655", display: "inline-block", boxShadow: "0 0 6px #FF4655" }} />
          <span className="font-orbitron" style={{ fontSize: "0.6rem", letterSpacing: "0.25em", color: "#FF4655" }}>
            SISTEMA ONLINE
          </span>
        </div>

        {/* Logo */}
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: "1rem", marginBottom: "0.75rem" }}>
          <span style={{ fontSize: "3rem", filter: "drop-shadow(0 0 12px rgba(255,70,85,0.5))" }}>🧠</span>
          <h1 className="font-orbitron" style={{
            fontSize: "clamp(2.5rem, 6vw, 4rem)", fontWeight: 900,
            letterSpacing: "0.08em", color: "#fff", margin: 0,
            textShadow: "0 0 40px rgba(255,70,85,0.3)",
          }}>
            DR. <span style={{ color: "#FF4655", textShadow: "0 0 30px rgba(255,70,85,0.6)" }}>K.</span>
          </h1>
          <span style={{ fontSize: "3rem", filter: "drop-shadow(0 0 12px rgba(139,92,246,0.5))" }}>🎮</span>
        </div>

        <p className="font-orbitron" style={{
          fontSize: "0.65rem", letterSpacing: "0.4em",
          textTransform: "uppercase", color: "#8B5CF6", margin: "0 0 1.25rem",
          textShadow: "0 0 20px rgba(139,92,246,0.4)",
        }}>
          Psicólogo Gamer™ &nbsp;·&nbsp; Diagnósticos desde 2025
        </p>

        <p style={{ fontSize: "0.95rem", color: "#94a3b8", maxWidth: "400px", margin: "0 auto", lineHeight: 1.7 }}>
          Diagnósticos psicológicos{" "}
          <span style={{ color: "#FF4655", fontWeight: 600 }}>100% fictícios</span>{" "}
          baseados na sua biblioteca Steam.
        </p>
        <p style={{ fontSize: "0.8rem", color: "#475569", marginTop: "0.35rem" }}>
          Completamente desnecessário. Absolutamente obrigatório.
        </p>
      </header>

      {/* ── MAIN CARD ── */}
      <section style={{
        position: "relative", zIndex: 1,
        display: "flex", alignItems: "center", justifyContent: "center",
        padding: "2.5rem 1rem 4rem",
      }}>
        <div className="fade-up-1 glow-pulse" style={{
          width: "100%", maxWidth: "500px",
          background: "linear-gradient(145deg, rgba(15,20,30,0.98) 0%, rgba(10,14,22,0.98) 100%)",
          border: "1px solid rgba(255,70,85,0.25)",
          borderRadius: "20px",
          boxShadow: "0 0 0 1px rgba(255,70,85,0.06), 0 32px 80px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.04)",
          overflow: "hidden",
        }}>

          {/* Title bar */}
          <div style={{
            padding: "0.875rem 1.375rem",
            background: "rgba(255,70,85,0.05)",
            borderBottom: "1px solid rgba(255,70,85,0.1)",
            display: "flex", alignItems: "center", justifyContent: "space-between",
          }}>
            <div style={{ display: "flex", gap: "0.45rem" }}>
              {["#FF5F57","#FEBC2E","#28C840"].map(c => (
                <div key={c} style={{
                  width: 12, height: 12, borderRadius: "50%", background: c,
                  boxShadow: `0 0 6px ${c}80`,
                }} />
              ))}
            </div>
            <span className="font-orbitron" style={{ fontSize: "0.58rem", letterSpacing: "0.22em", color: "#475569" }}>
              TERMINAL — DR.K/DIAGNOSE
            </span>
            <div style={{ width: 52 }} />
          </div>

          <div style={{ padding: "2rem" }}>
            <form onSubmit={handleSubmit}>
              <label className="font-orbitron" style={{
                display: "block", fontSize: "0.58rem", letterSpacing: "0.22em",
                color: "#64748B", marginBottom: "0.6rem", textTransform: "uppercase",
              }}>
                ID / URL do Perfil Steam
              </label>

              <div style={{ position: "relative", marginBottom: "0.5rem" }}>
                <input
                  type="text"
                  value={input}
                  onChange={e => setInput(e.target.value)}
                  disabled={isLoading}
                  placeholder="seu_nome ou URL do perfil"
                  autoComplete="off"
                  spellCheck={false}
                  style={{
                    width: "100%",
                    padding: "0.9rem 3rem 0.9rem 1.1rem",
                    background: "rgba(6,9,16,0.8)",
                    border: "1px solid rgba(255,70,85,0.2)",
                    borderRadius: "10px",
                    color: "#E2E8F0",
                    fontSize: "0.95rem",
                    fontFamily: "var(--font-inter), Inter, system-ui",
                    outline: "none",
                    transition: "border-color 0.2s, box-shadow 0.2s",
                  }}
                  onFocus={e => {
                    e.target.style.borderColor = "rgba(255,70,85,0.6)";
                    e.target.style.boxShadow = "0 0 0 3px rgba(255,70,85,0.1), 0 0 20px rgba(255,70,85,0.08)";
                  }}
                  onBlur={e => {
                    e.target.style.borderColor = "rgba(255,70,85,0.2)";
                    e.target.style.boxShadow = "none";
                  }}
                />
                {!input && !isLoading && (
                  <span className="cursor" style={{
                    position: "absolute", right: "1rem", top: "50%",
                    transform: "translateY(-50%)", color: "#FF4655", fontSize: "1.2rem",
                  }}>_</span>
                )}
              </div>

              <div style={{ marginBottom: "1.5rem" }} />

              {/* Loading progress */}
              {isLoading && (
                <div style={{
                  height: "3px", background: "rgba(255,70,85,0.08)",
                  borderRadius: "99px", marginBottom: "1.25rem",
                  overflow: "hidden",
                }}>
                  <div className="progress-bar" style={{
                    height: "100%", width: "45%",
                    background: "linear-gradient(90deg, transparent, #FF4655, #8B5CF6, transparent)",
                    borderRadius: "99px",
                  }} />
                </div>
              )}

              <button
                type="submit"
                disabled={isLoading || !input.trim()}
                style={{
                  width: "100%",
                  padding: "1rem 1.5rem",
                  background: isLoading || !input.trim()
                    ? "rgba(255,70,85,0.15)"
                    : "linear-gradient(135deg, #FF4655 0%, #e02030 60%, #c01828 100%)",
                  border: isLoading || !input.trim()
                    ? "1px solid rgba(255,70,85,0.2)"
                    : "1px solid rgba(255,70,85,0.5)",
                  borderRadius: "10px",
                  color: isLoading || !input.trim() ? "rgba(255,70,85,0.5)" : "#fff",
                  fontSize: "0.8rem",
                  fontFamily: "var(--font-orbitron), Orbitron, monospace",
                  fontWeight: 700,
                  letterSpacing: "0.18em",
                  textTransform: "uppercase",
                  cursor: isLoading || !input.trim() ? "not-allowed" : "pointer",
                  transition: "all 0.2s",
                  boxShadow: isLoading || !input.trim()
                    ? "none"
                    : "0 4px 24px rgba(255,70,85,0.4), 0 1px 0 rgba(255,255,255,0.12) inset",
                  display: "flex", alignItems: "center", justifyContent: "center", gap: "0.6rem",
                }}
                onMouseEnter={e => {
                  if (!isLoading && input.trim()) {
                    (e.currentTarget as HTMLButtonElement).style.transform = "translateY(-1px)";
                    (e.currentTarget as HTMLButtonElement).style.boxShadow = "0 8px 32px rgba(255,70,85,0.5), 0 1px 0 rgba(255,255,255,0.12) inset";
                  }
                }}
                onMouseLeave={e => {
                  (e.currentTarget as HTMLButtonElement).style.transform = "translateY(0)";
                  (e.currentTarget as HTMLButtonElement).style.boxShadow = isLoading || !input.trim()
                    ? "none"
                    : "0 4px 24px rgba(255,70,85,0.4), 0 1px 0 rgba(255,255,255,0.12) inset";
                }}
              >
                {isLoading ? (
                  <>
                    <svg className="spin" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                      <path d="M21 12a9 9 0 1 1-6.219-8.56" />
                    </svg>
                    {step === "loading_profile" ? "Buscando perfil..." : "Consultando Dr. K..."}
                  </>
                ) : "⚡ Me Diagnosticar"}
              </button>
            </form>

            {/* Error */}
            {error && (
              <div style={{
                marginTop: "1.25rem",
                padding: "0.875rem 1rem",
                background: "rgba(255,70,85,0.06)",
                border: "1px solid rgba(255,70,85,0.2)",
                borderRadius: "10px",
                display: "flex", gap: "0.6rem", alignItems: "flex-start",
              }}>
                <span style={{ fontSize: "1rem", flexShrink: 0 }}>⚠️</span>
                <span style={{ fontSize: "0.85rem", color: "#fca5a5", lineHeight: 1.6 }}>{error}</span>
              </div>
            )}

            {/* Stats */}
            <div style={{
              marginTop: "1.75rem",
              paddingTop: "1.5rem",
              borderTop: "1px solid rgba(255,70,85,0.08)",
              display: "grid", gridTemplateColumns: "1fr 1fr 1fr",
              textAlign: "center", gap: "0.5rem",
            }}>
              {STATS.map(s => (
                <div key={s.l}>
                  <div className="font-orbitron" style={{
                    fontSize: "1.5rem", fontWeight: 900, color: "#FF4655",
                    textShadow: "0 0 20px rgba(255,70,85,0.4)",
                  }}>{s.v}</div>
                  <div style={{ fontSize: "0.68rem", color: "#475569", marginTop: "0.15rem", letterSpacing: "0.04em" }}>{s.l}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ── FOOTER ── */}
      <footer style={{
        position: "relative", zIndex: 1, textAlign: "center",
        padding: "0 1rem 3rem",
      }}>
        <p style={{ fontSize: "0.72rem", color: "#334155", lineHeight: 1.8, maxWidth: "440px", margin: "0 auto" }}>
          ⚕️ O Dr. K. não possui CRM, formação médica ou qualquer credencial reconhecida.
          <br />Este site é <strong style={{ color: "#475569" }}>100% ficção</strong> e humor.
          <br /><span style={{ color: "#1e293b" }}>* Não é 100% científico. Na verdade, não é nem 1%.</span>
        </p>
      </footer>
    </main>
  );
}
