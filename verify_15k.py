import sys

def verify_cnf(cnf_file, sol_file):
    # Read the solution bitstring
    with open(sol_file, 'r') as f:
        sol_str = f.read().strip()
    
    # 0-indexed boolean array
    solution = [True if c == '1' else False for c in sol_str]
    n_vars = len(solution)

    # Read and verify the CNF
    satisfied_clauses = 0
    total_clauses = 0
    
    with open(cnf_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('c'):
                continue
            if line.startswith('p'):
                total_clauses = int(line.split()[3])
                continue
            
            # Parse clause
            literals = [int(x) for x in line.split() if x != '0']
            if not literals: continue
            
            clause_satisfied = False
            for lit in literals:
                var_idx = abs(lit) - 1 # 0-indexed
                is_positive = lit > 0
                if solution[var_idx] == is_positive:
                    clause_satisfied = True
                    break
                    
            if clause_satisfied:
                satisfied_clauses += 1
            else:
                print(f"Clause failed: {literals}")
                
    if satisfied_clauses == total_clauses:
        print(f"\n[SUCCESS] All {total_clauses} clauses are satisfied by the solution!")
        return True
    else:
        print(f"\n[FAILED] Only {satisfied_clauses}/{total_clauses} clauses satisfied.")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python verify_15k.py <problem_15k.cnf> <solution_15k.txt>")
        sys.exit(1)
    verify_cnf(sys.argv[1], sys.argv[2])
