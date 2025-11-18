#!/bin/bash
TARGET="$1"
PYTHON_SCRIPT="./scripts/parse_nmap_xml.py"

# --- 1. Validation and Setup ---
if [ -z "$TARGET" ]; then
  echo "Usage: $0 <target-or-network>"
  exit 1
fi

TIMESTAMP=$(date +%F_%T)
BASE_DIR=$(pwd) # Current directory is the project root
OUTDIR="$BASE_DIR/raw"
REPORTDIR="$BASE_DIR/reports"

# Ensure directories exist
mkdir -p "$OUTDIR" "$REPORTDIR"

SAFE_TARGET=${TARGET//\//_} # Makes filename safe (replaces / with _)
BASENAME="$OUTDIR/scan-$SAFE_TARGET-$TIMESTAMP"
SUMMARY_REPORT="$REPORTDIR/summary-$SAFE_TARGET-$TIMESTAMP.txt"
HTML_REPORT="$REPORTDIR/report-$SAFE_TARGET-$TIMESTAMP.html"

echo "================================================="
echo "Starting Automated Vulnerability Scan on $TARGET..."
echo "================================================="

# --- 2. Main Nmap Scan (Generates XML) ---
# -sS (Stealth Scan), -sV (Version), -A (Aggressive), --script vuln (Vulnerabilities)
sudo nmap -sS -sV -A --script "default,vuln" -T4 -oA "$BASENAME" "$TARGET"

if [ ! -f "$BASENAME.xml" ]; then
  echo "Error: Nmap XML output not found. Scan may have failed."
  exit 1
fi

# --- 3. Generate HTML Report (for visualization) ---
echo ""
echo "--- Generating Detailed HTML Report ---"
xsltproc "$BASENAME.xml" -o "$HTML_REPORT"
echo "HTML Report saved: $HTML_REPORT"

# --- 4. Generate Clean Text Summary (for quick analysis using Python) ---
echo ""
echo "--- Generating Clean Text Summary ---"
# Passes the XML file and the desired output path to the Python script
python3 "$PYTHON_SCRIPT" "$BASENAME.xml" "$SUMMARY_REPORT"

echo "================================================="
echo "PROCESS COMPLETE: Check the 'reports/' folder."
echo "================================================="
