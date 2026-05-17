"use client";

import { useState, useEffect, useRef } from "react";
import { createPortal } from "react-dom";
import { Diagnosis, encodeDiagnosis } from "../lib/codec";

interface Props { diagnosis: Diagnosis }

type CopyState = null | "link" | "text" | "challenge";

/* ── small action button ── */
function Btn({
  onClick, children, variant,
}: {
  onClick: () => void;
  children: React.ReactNode;
  variant: "red" | "purple";
}) {
  const [hover, setHover] = useState(false);
  const isRed = variant === "red";
  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        padding: "0.7rem 0.875rem",
        borderRadius: "10px",
        fontSize: "0.78rem",
        fontFamily: "var(--font-inter), Inter, system-ui",
        fontWeight: 500,
        cursor: "pointer",
        transition: "all 0.15s ease",
        display: "flex", alignItems: "center", justifyContent: "center", gap: "0.45rem",
        transform: hover ? "translateY(-1px)" : "translateY(0)",
        background: hover
          ? isRed
            ? "linear-gradient(135deg,#FF4655 0%,#e02030 100%)"
            : "linear-gradient(135deg,#8B5CF6 0%,#6d28d9 100%)"
          : isRed ? "rgba(255,70,85,0.1)" : "rgba(139,92,246,0.1)",
        border: hover
          ? isRed ? "1px solid rgba(255,70,85,0.7)" : "1px solid rgba(139,92,246,0.7)"
          : isRed ? "1px solid rgba(255,70,85,0.25)" : "1px solid rgba(139,92,246,0.25)",
        color: hover ? "#fff" : isRed ? "#fca5a5" : "#c4b5fd",
        boxShadow: hover
          ? isRed ? "0 4px 20px rgba(255,70,85,0.35)" : "0 4px 20px rgba(139,92,246,0.35)"
          : "none",
      }}
    >
      {children}
    </button>
  );
}

/* ── individual option inside the challenge popup ── */
function ChallengeOption({
  icon, label, sub, onClick, copied,
}: {
  icon: React.ReactNode;
  label: string;
  sub?: string;
  onClick: () => void;
  copied?: boolean;
}) {
  const [hover, setHover] = useState(false);
  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        width: "100%", display: "flex", alignItems: "center", gap: "0.875rem",
        padding: "0.75rem 1rem", borderRadius: "10px", cursor: "pointer",
        background: hover ? "rgba(255,255,255,0.04)" : "transparent",
        border: hover ? "1px solid rgba(255,255,255,0.08)" : "1px solid transparent",
        transition: "all 0.15s", textAlign: "left",
      }}
    >
      <span style={{
        width: 36, height: 36, borderRadius: "10px", flexShrink: 0,
        display: "flex", alignItems: "center", justifyContent: "center",
        fontSize: "1.1rem",
        background: "rgba(255,255,255,0.06)",
        border: "1px solid rgba(255,255,255,0.06)",
      }}>
        {copied ? "✓" : icon}
      </span>
      <div>
        <p style={{ margin: 0, fontSize: "0.875rem", color: copied ? "#86efac" : "#e2e8f0", fontWeight: 500 }}>
          {copied ? "Copiado!" : label}
        </p>
        {sub && !copied && (
          <p style={{ margin: 0, fontSize: "0.72rem", color: "#475569", marginTop: "0.1rem" }}>{sub}</p>
        )}
      </div>
    </button>
  );
}

/* ── challenge popup ── */
function ChallengePopup({
  onClose, originUrl, cid,
}: {
  onClose: () => void;
  originUrl: string;
  cid: string;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const [copied, setCopied] = useState(false);

  // close on outside click
  useEffect(() => {
    function handler(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) onClose();
    }
    document.addEventListener("mousedown", handler);
    return () => document.removeEventListener("mousedown", handler);
  }, [onClose]);

  // close on Escape
  useEffect(() => {
    function handler(e: KeyboardEvent) { if (e.key === "Escape") onClose(); }
    document.addEventListener("keydown", handler);
    return () => document.removeEventListener("keydown", handler);
  }, [onClose]);

  const challengeText = `Fui diagnosticado com "${cid}" pelo Dr. K. Psicólogo Gamer.\n\nE você? Qual é o seu diagnóstico? 🛋️🎮\n\n`;

  const openWhatsApp = () => {
    const text = encodeURIComponent(`${challengeText}${originUrl}`);
    window.open(`https://wa.me/?text=${text}`, "_blank", "noopener,noreferrer");
  };

  const openTelegram = () => {
    const params = new URLSearchParams({ url: originUrl, text: challengeText });
    window.open(`https://t.me/share/url?${params}`, "_blank", "noopener,noreferrer");
  };

  const openX = () => {
    const params = new URLSearchParams({ text: `${challengeText}`, url: originUrl });
    window.open(`https://twitter.com/intent/tweet?${params}`, "_blank", "noopener,noreferrer");
  };

  const copyChallenge = async () => {
    await navigator.clipboard.writeText(`${challengeText}${originUrl}`);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const content = (
    /* backdrop */
    <div style={{
      position: "fixed", inset: 0, zIndex: 9000,
      background: "rgba(0,0,0,0.85)",
      backdropFilter: "blur(8px)",
      display: "flex", alignItems: "center", justifyContent: "center",
      padding: "1rem",
    }}>
      {/* panel */}
      <div ref={ref} style={{
        width: "100%", maxWidth: "380px",
        background: "linear-gradient(160deg,rgba(13,18,28,0.99) 0%,rgba(8,12,20,0.99) 100%)",
        border: "1px solid rgba(139,92,246,0.25)",
        borderRadius: "18px",
        boxShadow: "0 0 0 1px rgba(139,92,246,0.06), 0 40px 80px rgba(0,0,0,0.7)",
        overflow: "hidden",
        animation: "fadeUp 0.25s cubic-bezier(0.16,1,0.3,1) both",
      }}>
        {/* header */}
        <div style={{
          padding: "1rem 1.25rem",
          borderBottom: "1px solid rgba(139,92,246,0.1)",
          background: "rgba(139,92,246,0.04)",
          display: "flex", alignItems: "center", justifyContent: "space-between",
        }}>
          <div>
            <p className="font-orbitron" style={{ margin: 0, fontSize: "0.75rem", fontWeight: 700, color: "#c4b5fd", letterSpacing: "0.05em" }}>
              ⚔️ Desafiar amigo
            </p>
            <p style={{ margin: 0, fontSize: "0.72rem", color: "#475569", marginTop: "0.2rem" }}>
              Escolha como compartilhar
            </p>
          </div>
          <button
            onClick={onClose}
            style={{
              width: 30, height: 30, borderRadius: "8px",
              background: "rgba(255,255,255,0.04)",
              border: "1px solid rgba(255,255,255,0.06)",
              color: "#64748B", fontSize: "1rem", cursor: "pointer",
              display: "flex", alignItems: "center", justifyContent: "center",
              transition: "all 0.15s",
            }}
          >
            ✕
          </button>
        </div>

        {/* options */}
        <div style={{ padding: "0.75rem" }}>
          <ChallengeOption
            icon="💬"
            label="WhatsApp"
            sub="Abre o app diretamente"
            onClick={openWhatsApp}
          />
          <ChallengeOption
            icon={<span style={{ fontWeight: 900, fontSize: "0.95rem" }}>𝕏</span>}
            label="X (Twitter)"
            sub="Posta um tweet de desafio"
            onClick={openX}
          />
          <ChallengeOption
            icon={
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 0 0-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06-.01.24-.02.27z" fill="#64b5f6"/>
              </svg>
            }
            label="Telegram"
            sub="Envia para um contato ou grupo"
            onClick={openTelegram}
          />
          <div style={{ height: "1px", background: "rgba(255,255,255,0.04)", margin: "0.4rem 0" }} />
          <ChallengeOption
            icon="🔗"
            label="Copiar link de desafio"
            sub="Compartilhe onde quiser"
            onClick={copyChallenge}
            copied={copied}
          />
        </div>
      </div>
    </div>
  );

  return createPortal(content, document.body);
}

/* ── main export ── */
export default function ShareButton({ diagnosis }: Props) {
  const [copied, setCopied]           = useState<CopyState>(null);
  const [showChallenge, setShowChallenge] = useState(false);

  const getUrl    = () => `${window.location.origin}/resultado/${encodeDiagnosis(diagnosis)}`;
  const getOrigin = () => window.location.origin;

  const copyLink = async () => {
    await navigator.clipboard.writeText(getUrl());
    setCopied("link");
    setTimeout(() => setCopied(null), 2000);
  };

  const copyText = async () => {
    const url = getUrl();
    const text =
      `🛋️ DIAGNÓSTICO GAMER™ — Dr. K. Psicólogo da Steam\n\n` +
      `👤 Paciente: ${diagnosis.patient}\n` +
      `🧠 CID: ${diagnosis.cid}\n\n` +
      `📋 Sintomas:\n${diagnosis.symptoms.map((s, i) => `${i + 1}. ${s}`).join("\n")}\n\n` +
      `📊 Prognóstico: ${diagnosis.prognosis}\n\n` +
      `💊 Remédio: ${diagnosis.remedy}\n\n` +
      `🔗 ${url}`;
    await navigator.clipboard.writeText(text);
    setCopied("text");
    setTimeout(() => setCopied(null), 2000);
  };

  return (
    <>
      <div style={{ width: "100%", maxWidth: "580px" }}>
        {/* section divider */}
        <div style={{ display: "flex", alignItems: "center", gap: "0.75rem", marginBottom: "0.875rem" }}>
          <div style={{ flex: 1, height: "1px", background: "rgba(255,70,85,0.08)" }} />
          <span className="font-orbitron" style={{ fontSize: "0.56rem", letterSpacing: "0.25em", color: "#334155" }}>
            AÇÕES DO LAUDO
          </span>
          <div style={{ flex: 1, height: "1px", background: "rgba(255,70,85,0.08)" }} />
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: "0.5rem" }}>
          <Btn onClick={copyLink} variant="red">
            🔗 {copied === "link" ? "Copiado!" : "Copiar link"}
          </Btn>
          <Btn onClick={copyText} variant="red">
            📋 {copied === "text" ? "Copiado!" : "Copiar texto"}
          </Btn>
          <Btn onClick={() => setShowChallenge(true)} variant="purple">
            ⚔️ Desafiar amigo
          </Btn>
        </div>
      </div>

      {showChallenge && (
        <ChallengePopup
          onClose={() => setShowChallenge(false)}
          originUrl={getOrigin()}
          cid={diagnosis.cid}
        />
      )}
    </>
  );
}
