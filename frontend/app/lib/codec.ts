/**
 * Serializa e desserializa o diagnóstico via base64url para compartilhamento.
 * Suporta corretamente UTF-8 (nomes com acentos, emojis, etc).
 */

export interface Diagnosis {
  patient: string;
  cid: string;
  symptoms: string[];
  prognosis: string;
  remedy: string;
  dominant_categories: string[];
  special_flags: string[];
  total_games: number;
}

export function encodeDiagnosis(diagnosis: Diagnosis): string {
  const json = JSON.stringify(diagnosis);
  // encodeURIComponent → UTF-8 percent-encoded → unescape → latin-1 safe for btoa
  const base64 = btoa(unescape(encodeURIComponent(json)));
  return base64.replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

export function decodeDiagnosis(hash: string): Diagnosis | null {
  try {
    if (!hash || hash.length > 8192) return null; // limite de tamanho
    const base64 = hash.replace(/-/g, "+").replace(/_/g, "/");
    const json = decodeURIComponent(escape(atob(base64)));
    const obj = JSON.parse(json);
    // Validação mínima de estrutura
    if (
      typeof obj.patient !== "string" ||
      typeof obj.cid !== "string" ||
      !Array.isArray(obj.symptoms) ||
      typeof obj.prognosis !== "string" ||
      typeof obj.remedy !== "string"
    ) {
      return null;
    }
    return obj as Diagnosis;
  } catch {
    return null;
  }
}
