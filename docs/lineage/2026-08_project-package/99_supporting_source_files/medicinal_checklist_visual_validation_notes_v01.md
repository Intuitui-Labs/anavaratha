# Medicinal checklist visual validation notes

## Batch 1: PDF pages 10–15

The Appendix 1 table begins on PDF page 10, printed page 73, and continues through the remaining article pages. The header is repeated on each page. The visible columns are, in order: Updated Family; Family name in Flora; Updated Scientific Name; Scientific Name in Flora; Homotypic Synonyms; Local Name (Sinhala); Status 2012; Status 2020.

The first pages show that rows are not one text line each. Scientific names, author citations, synonyms, and local names frequently wrap across multiple lines. Family names often appear only on the first row of a family group, while continuation rows leave the family cell blank. Some taxonomic records have blank earlier-Flora or synonym fields. Endemic taxa appear in bold in the original PDF, so bold formatting should not be mistaken for text content or discarded without noting that it is a source signal.

The PDF text layer preserves approximate column spacing but can split one row across several lines. A row-level parser must therefore use positional alignment and continuation logic, not line-by-line splitting alone. Visual checks confirmed examples including multi-line synonyms for *Asystasia variabilis*, family continuation from Acanthaceae across pages 10–11, a family transition to Achariaceae on page 12, and several records with blank status cells in the 2020 column. Status values must be read from their own columns and not inferred when absent.

No medicinal use, habitat, seasonality, propagation method, or cultivation recommendation should be inferred from inclusion in Appendix 1. Those fields require separate sources under the Anavaratha verification protocol.

## Batch 2: PDF pages 23–25

The later spot check confirms that the same structural cautions persist well beyond the opening pages. Scientific names may begin on the same visual baseline as the last plain-font author fragment of the previous record, which means row starts cannot be identified safely by looking only at the first token in the scientific-name column. This was visible in pages where a new italic genus follows a plain citation fragment within the same horizontal line. The extractor therefore needs to detect the first italic uppercase genus anywhere within the scientific-name cell, not only at the leftmost token.

These pages also confirm that several rows have blank status cells, blank earlier-Flora cells, or blank synonym cells. Some local names extend across multiple words or comma-separated variants. Family changes remain visually clear in the first column, but continuation rows leave family cells empty. The parser must therefore carry family context cautiously and never assume that a blank cell means missing taxonomic identity rather than continuation.

## Batch 3: PDF pages 50–52 and 100–102

Mid-table and later-table spot checks confirm that the basic column structure remains stable across the Appendix. The same x-position bands continue to separate updated family, earlier family, updated scientific name, earlier scientific name, homotypic synonyms, Sinhala local names, and 2012/2020 status fields. This supports a coordinate-based extraction approach rather than page-specific templates.

However, these pages also show several continuing risks. Dense synonym clusters can occupy many wrapped lines; some rows carry updated and earlier scientific names simultaneously; some status columns are blank on one side; and certain names marked with an asterisk or boldface can change the visual texture of the line without changing its taxonomic role. The PDF therefore appears suitable for structured extraction with page provenance, but not for fully automatic validation. The present output should be treated as a machine-extracted draft crosswalk requiring further sampling and record-level review, not as a final authoritative table.

## Targeted row validation: PDF pages 26 and 71

Page 26 confirms that Aponogetonaceae contains two distinct records—*Aponogeton crispus* and bold *Aponogeton jacobsenii*—with separate Sinhala local-name and 2012/2020 status cells. It also confirms that a long local-name string such as “Panu-habarala, nai-habarala, Gaha-ala” can extend visually toward the status area without being a status value. The revised coordinate/token classification correctly keeps these as local-name content and preserves the separate status columns.

Page 71 confirms the closely spaced Indigofera rows, including *Indigofera hirsuta*, *Indigofera tinctoria*, and *Indigofera trita*. The printed PDF visually shows separate rows and separate LC/LC status pairs. The earlier merged `LC LC` anomaly was caused by the embedded text layer’s lowercased `lndigofera` token and is now separated by the narrow OCR fallback. This targeted check supports the revised parser for that anomaly but does not eliminate the need for broader review of unusual typography and page transitions.

## Targeted row validation: PDF pages 10 and 148

Page 10 confirms the Appendix 1 opening header, Acanthaceae family start, multi-line synonyms, Sinhala local names, and separate 2012/2020 status columns. It also confirms that the table includes records with blank status fields, so blank status must be preserved rather than imputed.

Page 148 confirms that the extractor reaches the table’s final page and final visible records, including Zygophyllaceae and Simaroubaceae, with *Balanites aegyptiaca* as the final visible record. The last page also contains long synonym blocks and several blank status fields, reinforcing the need to retain page provenance and avoid treating the end of the table as a simple one-line list.
