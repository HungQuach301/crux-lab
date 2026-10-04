// C5 film page: values the signed engines fetched at module load in C3/C4 (top-level await) are given here instead, before the
// engines are evaluated (build_page.mjs rewrites those two lines to window.TOK_E / window.DATA_H2 / window.DATA_H3).
import tok from '../../design/c3/final/tokens.json';
import card from './method_card.json';
window.TOK_E = tok;
window.CARD_E = card;
