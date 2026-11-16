const base = import.meta.env.BASE_URL.replace(/\/$/, '');
export const u = (p: string) => `${base}${p.startsWith('/') ? p : '/' + p}`;
export const STAGE = 'Sensemaking';
