import { decodeDiagnosis } from "../../lib/codec";
import DiagnosisCard from "../../components/DiagnosisCard";
import ShareButton from "../../components/ShareButton";
import Link from "next/link";
import { notFound } from "next/navigation";

interface Props { params: Promise<{ hash: string }> }

export default async function ResultadoPage({ params }: Props) {
  const { hash } = await params;
  const diagnosis = decodeDiagnosis(hash);
  if (!diagnosis) notFound();

  return (
    <main style={{ minHeight: "100vh", background: "#060910", position: "relative", overflow: "hidden" }}>

      {/* ── Ambient glows ── */}
      <div aria-hidden style={{ position: "fixed", inset: 0, pointerEvents: "none", zIndex: 0 }}>
        <div style={{
          position: "absolute", top: "-15%", left: "50%", transform: "translateX(-50%)",
          width: "800px", height: "500px",
          background: "radial-gradient(ellipse, rgba(255,70,85,0.1) 0%, transparent 65%)",
        }} />
        <div style={{
          position: "absolute", bottom: 0, right: "-5%",
          width: "500px", height: "500px",
          background: "radial-gradient(ellipse, rgba(139,92,246,0.07) 0%, transparent 60%)",
        }} />
        <div className="bg-grid" style={{ position: "absolute", inset: 0, opacity: 0.4 }} />
      </div>

      <div style={{
        position: "relative", zIndex: 1,
        display: "flex", flexDirection: "column", alignItems: "center",
        padding: "2.5rem 1rem 4rem", gap: "1.5rem",
      }}>

        {/* ── Mini header ── */}
        <div className="fade-up" style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: "0.5rem" }}>
          <Link
            href="/"
            style={{ display: "flex", alignItems: "center", gap: "0.6rem", textDecoration: "none" }}
          >
            <span style={{ fontSize: "2rem", filter: "drop-shadow(0 0 8px rgba(255,70,85,0.4))" }}>🧠</span>
            <span className="font-orbitron" style={{
              fontSize: "1.5rem", fontWeight: 900, letterSpacing: "0.1em", color: "#fff",
              textShadow: "0 0 30px rgba(255,70,85,0.25)",
            }}>
              DR. <span style={{ color: "#FF4655" }}>K.</span>
            </span>
            <span style={{ fontSize: "2rem", filter: "drop-shadow(0 0 8px rgba(139,92,246,0.4))" }}>🎮</span>
          </Link>

          <div style={{
            display: "inline-flex", alignItems: "center", gap: "0.4rem",
            padding: "0.25rem 0.75rem", borderRadius: "99px",
            background: "rgba(139,92,246,0.08)", border: "1px solid rgba(139,92,246,0.2)",
          }}>
            <span style={{ width: 5, height: 5, borderRadius: "50%", background: "#8B5CF6", display: "inline-block", boxShadow: "0 0 6px #8B5CF6" }} />
            <span className="font-orbitron" style={{ fontSize: "0.58rem", letterSpacing: "0.3em", color: "#8B5CF6" }}>
              LAUDO OFICIAL EMITIDO
            </span>
          </div>
        </div>

        {/* ── Card ── */}
        <div className="fade-up-2" style={{ width: "100%" , display: "flex", justifyContent: "center" }}>
          <DiagnosisCard diagnosis={diagnosis} />
        </div>

        {/* ── Actions ── */}
        <div className="fade-up-3" style={{ width: "100%", display: "flex", justifyContent: "center" }}>
          <ShareButton diagnosis={diagnosis} />
        </div>

        {/* ── Back link ── */}
        <div className="fade-up-4">
          <Link
            href="/"
            className="back-link"
            style={{
              display: "inline-flex", alignItems: "center", gap: "0.4rem",
              fontSize: "0.75rem", letterSpacing: "0.06em",
              padding: "0.4rem 0.75rem",
              border: "1px solid rgba(255,255,255,0.05)",
              borderRadius: "8px",
            }}
          >
            ← Diagnosticar outro jogador
          </Link>
        </div>

        <p style={{
          fontSize: "0.68rem", color: "rgba(71,85,105,0.5)",
          textAlign: "center", maxWidth: "380px", lineHeight: 1.7,
        }}>
          Laudo emitido pelo Dr. K., que não possui nenhuma credencial médica real.
          Este diagnóstico é 100% fictício e para fins de entretenimento.
        </p>
      </div>
    </main>
  );
}

export async function generateMetadata({ params }: Props) {
  const { hash } = await params;
  const diagnosis = decodeDiagnosis(hash);
  if (!diagnosis) return {};
  return {
    title: `${diagnosis.patient} — ${diagnosis.cid} | Dr. K.`,
    description: `Diagnóstico: ${diagnosis.cid}. ${diagnosis.prognosis}`,
  };
}
