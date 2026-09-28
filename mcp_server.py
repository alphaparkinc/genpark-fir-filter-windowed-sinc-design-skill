"""MCP stdio server for FIR Filter Designer."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import FIRFilterDesign

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "design_fir_lowpass",
                        "description": "Design linear-phase FIR filter coefficients using Hamming-windowed sinc",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "num_taps": {"type": "integer", "description": "Number of taps (must be odd)", "default": 21},
                                "cutoff_ratio": {"type": "number", "description": "Normalized cutoff (0 to 1)", "default": 0.2}
                            },
                            "required": ["num_taps", "cutoff_ratio"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "design_fir_lowpass":
            taps = int(args.get("num_taps", 21))
            cut = float(args.get("cutoff_ratio", 0.2))
            c = FIRFilterDesign.design_lowpass(taps, cut)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"coefficients": c, "num_taps": taps}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
