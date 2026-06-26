#!/usr/bin/env python3
"""
Comprehensive documentation generator for 90 NeetCode submission folders.
Analyzes code, adds docstrings, inline comments, and generates README files.
"""

import os
import ast
import re
from pathlib import Path
from typing import Optional, Tuple, List, Dict
import sys

# Base directory for submissions
BASE_DIR = Path("/Users/mikenguyen/Projects/neetcode-submissions/Data Structures & Algorithms")

class SubmissionDocumenter:
    """Handles documentation for individual submission folders."""
    
    def __init__(self, folder_path: Path):
        self.folder_path = folder_path
        self.folder_name = folder_path.name
        self.submission_file = self._find_latest_submission()
        self.code_content = None
        self.tree = None
        self.function_name = None
        self.algorithm_info = {}
        
    def _find_latest_submission(self) -> Optional[Path]:
        """Find the latest submission file (submission-N.py with highest N)."""
        submission_files = list(self.folder_path.glob("submission-*.py"))
        if not submission_files:
            return None
        
        # Sort by number to get latest
        def get_number(path):
            match = re.search(r'submission-(\d+)\.py', path.name)
            return int(match.group(1)) if match else 0
        
        return max(submission_files, key=get_number)
    
    def read_code(self) -> bool:
        """Read the submission file."""
        if not self.submission_file:
            return False
        
        try:
            with open(self.submission_file, 'r') as f:
                self.code_content = f.read()
            self.tree = ast.parse(self.code_content)
            return True
        except Exception as e:
            print(f"Error reading {self.submission_file}: {e}")
            return False
    
    def extract_function_info(self) -> bool:
        """Extract function name and parameters from AST."""
        if not self.tree:
            return False
        
        try:
            for node in ast.walk(self.tree):
                if isinstance(node, ast.ClassDef) and node.name == "Solution":
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef) and item.name != "__init__":
                            self.function_name = item.name
                            return True
            return False
        except Exception as e:
            print(f"Error extracting function info: {e}")
            return False
    
    def analyze_algorithm(self) -> Dict:
        """Analyze the algorithm based on code patterns."""
        if not self.code_content:
            return {}
        
        analysis = {
            "algorithm": "Algorithm",
            "steps": [],
            "time_complexity": "O(n)",
            "time_explanation": "depends on problem constraints",
            "space_complexity": "O(1)",
            "space_explanation": "minimal extra space used"
        }
        
        code_lower = self.code_content.lower()
        
        # Detect algorithm patterns
        if "queue" in code_lower or "deque" in code_lower:
            if "visited" in code_lower or "level" in code_lower:
                analysis["algorithm"] = "BFS (Breadth-First Search)"
                analysis["time_complexity"] = "O(V + E)"
                analysis["time_explanation"] = "visit each vertex and edge once"
                analysis["space_complexity"] = "O(V)"
                analysis["space_explanation"] = "queue can contain up to V vertices"
            else:
                analysis["algorithm"] = "Queue-based"
                analysis["time_complexity"] = "O(n)"
                analysis["space_complexity"] = "O(n)"
        
        elif "stack" in code_lower or ("append" in code_lower and "pop" in code_lower):
            if "postorder" in code_lower or "inorder" in code_lower:
                analysis["algorithm"] = "Tree Traversal (Stack-based)"
                analysis["time_complexity"] = "O(n)"
                analysis["time_explanation"] = "visit each node once"
                analysis["space_complexity"] = "O(h)"
                analysis["space_explanation"] = "stack depth equals tree height"
            else:
                analysis["algorithm"] = "Stack-based"
                analysis["time_complexity"] = "O(n)"
                analysis["space_complexity"] = "O(n)"
        
        elif "sort" in code_lower:
            analysis["algorithm"] = "Sorting"
            analysis["time_complexity"] = "O(n log n)"
            analysis["time_explanation"] = "standard sorting complexity"
            analysis["space_complexity"] = "O(1) or O(n)"
            analysis["space_explanation"] = "depends on sorting algorithm"
        
        elif "binary" in code_lower and "search" in code_lower:
            analysis["algorithm"] = "Binary Search"
            analysis["time_complexity"] = "O(log n)"
            analysis["time_explanation"] = "halve search space each iteration"
            analysis["space_complexity"] = "O(1)"
            analysis["space_explanation"] = "iterative approach uses constant space"
        
        elif "dp" in code_lower or "memo" in code_lower or "cache" in code_lower:
            if "memo" in code_lower or "cache" in code_lower:
                analysis["algorithm"] = "Dynamic Programming (Memoization)"
            else:
                analysis["algorithm"] = "Dynamic Programming"
            analysis["time_complexity"] = "O(n)"
            analysis["time_explanation"] = "compute each subproblem once"
            analysis["space_complexity"] = "O(n)"
            analysis["space_explanation"] = "store results for each subproblem"
        
        elif "recursive" in code_lower or "backtrack" in code_lower:
            analysis["algorithm"] = "Backtracking"
            analysis["time_complexity"] = "O(2^n)"
            analysis["time_explanation"] = "exponential search space"
            analysis["space_complexity"] = "O(n)"
            analysis["space_explanation"] = "recursion depth and result storage"
        
        elif "dict" in code_lower or "hash" in code_lower or "{" in code_lower:
            analysis["algorithm"] = "Hash Table/Dictionary"
            analysis["time_complexity"] = "O(n)"
            analysis["time_explanation"] = "linear scan plus hash operations"
            analysis["space_complexity"] = "O(n)"
            analysis["space_explanation"] = "store up to n elements"
        
        elif "two" in code_lower and "pointer" in code_lower:
            analysis["algorithm"] = "Two Pointers"
            analysis["time_complexity"] = "O(n)"
            analysis["time_explanation"] = "single pass with two pointers"
            analysis["space_complexity"] = "O(1)"
            analysis["space_explanation"] = "only use constant extra space"
        
        elif "sliding" in code_lower and "window" in code_lower:
            analysis["algorithm"] = "Sliding Window"
            analysis["time_complexity"] = "O(n)"
            analysis["time_explanation"] = "window slides through array once"
            analysis["space_complexity"] = "O(k)"
            analysis["space_explanation"] = "store elements in window"
        
        elif "while" in code_lower and "carry" in code_lower:
            analysis["algorithm"] = "Iteration with Carry"
            analysis["time_complexity"] = "O(max(m, n))"
            analysis["time_explanation"] = "process all elements of both inputs"
            analysis["space_complexity"] = "O(max(m, n))"
            analysis["space_explanation"] = "output length equals max input length"
        
        elif "linked" in code_lower and "list" in code_lower:
            analysis["algorithm"] = "Linked List Manipulation"
            analysis["time_complexity"] = "O(n)"
            analysis["time_explanation"] = "traverse the linked list"
            analysis["space_complexity"] = "O(1) or O(n)"
            analysis["space_explanation"] = "depends on whether new list created"
        
        else:
            # Generic analysis
            if "for" in code_lower and "for" in code_lower[code_lower.index("for")+1:]:
                analysis["time_complexity"] = "O(n^2)"
                analysis["time_explanation"] = "nested loops over input"
                analysis["space_complexity"] = "O(1) to O(n)"
            else:
                analysis["time_complexity"] = "O(n)"
                analysis["time_explanation"] = "linear scan of input"
        
        return analysis
    
    def generate_docstring(self) -> str:
        """Generate comprehensive docstring."""
        self.algorithm_info = self.analyze_algorithm()
        
        time_c = self.algorithm_info.get('time_complexity', 'n')
        space_c = self.algorithm_info.get('space_complexity', '1')
        
        docstring = f'''"""
{self._get_problem_description()}.

Algorithm: {self.algorithm_info.get('algorithm', 'Algorithm')}
- Approach: {self._get_approach()}
- Key Operations: {self._get_key_operations()}

Time Complexity: {time_c} - {self.algorithm_info.get('time_explanation', 'varies')}
Space Complexity: {space_c} - {self.algorithm_info.get('space_explanation', 'minimal')}
"""'''
        
        return docstring
    
    def _get_problem_description(self) -> str:
        """Generate problem description from folder name."""
        words = self.folder_name.replace('-', ' ').title()
        return f"Solves the {words} problem"
    
    def _get_approach(self) -> str:
        """Get approach description."""
        algo = self.algorithm_info.get('algorithm', '')
        approaches = {
            "BFS": "Use queue for level-order traversal",
            "DFS": "Use recursion or stack for depth-first exploration",
            "Binary Search": "Divide search space in half each iteration",
            "Dynamic Programming": "Build solution bottom-up using subproblems",
            "Backtracking": "Explore all possibilities with pruning",
            "Hash Table": "Map values for O(1) lookup",
            "Two Pointers": "Move two pointers from opposite ends",
            "Sliding Window": "Maintain window of relevant elements"
        }
        return approaches.get(algo, "Implement algorithm efficiently")
    
    def _get_key_operations(self) -> str:
        """Get key operations description."""
        code_lower = self.code_content.lower() if self.code_content else ""
        
        if "append" in code_lower:
            return "insert nodes/elements into result structure"
        elif "while" in code_lower:
            return "iterate through input with conditions"
        elif "recursive" in code_lower or "def " in code_lower:
            return "recursive exploration with memoization"
        else:
            return "sequential processing of input"
    
    def add_docstring_to_code(self) -> bool:
        """Add docstring to the main function."""
        if not self.code_content or not self.function_name:
            return False
        
        try:
            # Find the function definition line
            lines = self.code_content.split('\n')
            func_line_idx = None
            
            for i, line in enumerate(lines):
                if f"def {self.function_name}" in line:
                    func_line_idx = i
                    break
            
            if func_line_idx is None:
                return False
            
            # Find the end of function signature (the line with ':')
            sig_end = func_line_idx
            for i in range(func_line_idx, len(lines)):
                if ':' in lines[i]:
                    sig_end = i
                    break
            
            # Check if there's already a docstring
            if sig_end + 1 < len(lines):
                next_line = lines[sig_end + 1].strip()
                if next_line.startswith('"""') or next_line.startswith("'''"):
                    # Docstring already exists
                    return True
            
            # Get base indentation
            func_line = lines[func_line_idx]
            func_indent = len(func_line) - len(func_line.lstrip())
            docstring_indent = ' ' * (func_indent + 4)
            
            # Create docstring with proper indentation
            docstring = self.generate_docstring()
            # Re-indent the docstring
            docstring_lines = docstring.split('\n')
            indented_docstring = '\n'.join([docstring_indent + line if line.strip() else line for line in docstring_lines])
            
            # Insert docstring after function signature
            lines.insert(sig_end + 1, indented_docstring)
            
            # Add inline comments for key logic
            lines = self._add_inline_comments(lines, sig_end + 2)
            
            self.code_content = '\n'.join(lines)
            return True
        except Exception as e:
            print(f"Error adding docstring: {e}")
            return False
    
    def _add_inline_comments(self, lines: List[str], func_start: int) -> List[str]:
        """Add inline comments for key logic."""
        # Find key patterns and add comments
        i = func_start
        while i < len(lines):
            line = lines[i]
            stripped = line.lstrip()
            
            # Skip empty lines and docstrings
            if not stripped or stripped.startswith('"""') or stripped.startswith("'''"):
                i += 1
                continue
            
            # Add comments for loops
            if stripped.startswith('while ') or stripped.startswith('for '):
                indent = len(line) - len(stripped)
                if '# ' not in line:
                    if stripped.startswith('while'):
                        comment = '# Iterate until condition fails'
                    elif 'range' in stripped:
                        comment = '# Process each element'
                    else:
                        comment = '# Iterate through collection'
                    lines[i] = line + '  ' + comment
            
            # Add comments for important operations
            elif any(op in stripped for op in ['carry =', 'visited', 'memo', 'cache']):
                if '# ' not in line:
                    if 'carry' in stripped:
                        comment = '# Track carry for addition'
                    elif 'visited' in stripped:
                        comment = '# Mark node/element as visited'
                    elif 'memo' in stripped or 'cache' in stripped:
                        comment = '# Store computed results'
                    else:
                        comment = '# Important operation'
                    lines[i] = line + '  ' + comment
            
            i += 1
        
        return lines
    
    def write_code(self) -> bool:
        """Write the modified code back to file."""
        if not self.code_content or not self.submission_file:
            return False
        
        try:
            with open(self.submission_file, 'w') as f:
                f.write(self.code_content)
            return True
        except Exception as e:
            print(f"Error writing code: {e}")
            return False
    
    def generate_readme(self) -> bool:
        """Generate comprehensive README.md."""
        if not self.code_content:
            return False
        
        title = self.folder_name.replace('-', ' ').title()
        
        # Extract problem context from code
        problem_desc = self._infer_problem_description()
        example = self._infer_example()
        
        readme_content = f"""# {title}

## Problem Description

{problem_desc}

### Example
```
{example}
```

## Algorithm Explanation

### Approach: {self.algorithm_info.get('algorithm', 'Algorithm')}

The solution uses **{self.algorithm_info.get('algorithm', 'Algorithm').lower()}** to solve this problem efficiently.

**Key Steps:**
1. **Initialize**: Set up necessary data structures
2. **Process**: Apply the algorithm logic
3. **Return**: Construct and return the result

**Algorithm Pattern:**
- {self._get_approach()}
- Use appropriate data structures for efficient access
- Handle edge cases (empty input, single element, etc.)

## Complexity Analysis

### Time Complexity: {self.algorithm_info.get('time_complexity', 'O(n)')}
- **Explanation**: {self.algorithm_info.get('time_explanation', 'Varies based on problem constraints')}
- Each operation in the main loop runs in constant time
- The loop itself runs for all relevant elements/iterations

### Space Complexity: {self.algorithm_info.get('space_complexity', 'O(1)')}
- **Explanation**: {self.algorithm_info.get('space_explanation', 'Minimal extra space required')}
- Primary space usage: {self._get_space_usage()}

## Visual Representation

```
Problem Input:
├── Parse/Validate input
├── Initialize data structure
│
├── Main Algorithm Loop:
│   ├── Process current element
│   ├── Update state/structure
│   └── Move to next element
│
└── Return Result:
    └── Output processed data
```

## Key Insights

1. **Algorithm Selection**: {self._get_algorithm_insight()}
2. **Edge Cases**: Handle empty inputs, single elements, and boundary conditions
3. **Data Structures**: {self._get_data_structure_insight()}
4. **Optimization**: {self._get_optimization_insight()}

## Implementation Details

- **Function Name**: `{self.function_name or 'solve'}`
- **Input Parameters**: Properly typed according to problem requirements
- **Output**: Returns result in expected format
- **Edge Cases**: Handles empty inputs and boundary conditions

## Common Patterns Used

- Initialize pointer or counter variables
- Iterate through input data
- Update state based on algorithm logic
- Return computed result

## Testing Strategy

1. Test with empty input (if applicable)
2. Test with single element
3. Test with typical case
4. Test with edge cases (maximum values, etc.)
5. Verify both correctness and complexity requirements

"""
        
        try:
            readme_path = self.folder_path / "README.md"
            with open(readme_path, 'w') as f:
                f.write(readme_content)
            return True
        except Exception as e:
            print(f"Error writing README: {e}")
            return False
    
    def _infer_problem_description(self) -> str:
        """Infer problem description from folder name and code."""
        name_parts = self.folder_name.replace('-', ' ')
        
        descriptions = {
            "two integer sum": "Given an array of integers, find two numbers that add up to a target value.",
            "two integer sum ii": "Find two numbers in a sorted array that add up to a target value.",
            "three integer sum": "Find all triplets in an array that sum to a target value.",
            "add two numbers": "Add two numbers represented as linked lists (with digits in reverse order).",
            "binary search": "Find a target value in a sorted array using binary search.",
            "binary tree": "Perform operations on binary tree structures.",
            "climbing stairs": "Determine the number of ways to climb stairs.",
            "coin change": "Find the minimum number of coins to make a target amount.",
            "island": "Count or identify connected components (islands) in a grid.",
            "anagram": "Group words into anagrams or identify anagram relationships.",
            "parentheses": "Validate or generate valid parentheses combinations.",
            "trapping water": "Calculate water trapped between elevation levels.",
            "valid": "Validate whether input meets certain criteria.",
        }
        
        for key, desc in descriptions.items():
            if key in name_parts.lower():
                return desc
        
        return f"Solve the {name_parts} problem efficiently."
    
    def _infer_example(self) -> str:
        """Infer example from code and folder name."""
        name_parts = self.folder_name.lower()
        
        examples = {
            "two integer sum": "Input: nums = [2, 7, 11, 15], target = 9\nOutput: [0, 1]  # because nums[0] + nums[1] = 9",
            "binary search": "Input: nums = [1, 3, 5, 7], target = 5\nOutput: 2",
            "climbing stairs": "Input: n = 3\nOutput: 3  # [1,1,1], [1,2], [2,1]",
            "coin change": "Input: coins = [1, 2, 5], amount = 5\nOutput: 1  # just one 5-coin",
            "parentheses": "Input: n = 2\nOutput: ['(())', '()()']",
            "island": "Input: Grid with 0s and 1s\nOutput: Number of connected islands",
        }
        
        for key, example in examples.items():
            if key in name_parts:
                return example
        
        return "Input: Problem-specific input\nOutput: Expected solution"
    
    def _get_space_usage(self) -> str:
        """Get space usage description."""
        algo = self.algorithm_info.get('algorithm', '').lower()
        if 'queue' in algo or 'bfs' in algo:
            return "queue stores nodes at current level (O(width))"
        elif 'stack' in algo or 'dfs' in algo:
            return "recursion/stack depth equals tree height (O(height))"
        elif 'dp' in algo or 'dynamic' in algo:
            return "DP table stores results for all subproblems"
        elif 'hash' in algo:
            return "hash table stores key-value mappings"
        else:
            return "minimal auxiliary space"
    
    def _get_algorithm_insight(self) -> str:
        """Get algorithm selection insight."""
        algo = self.algorithm_info.get('algorithm', '')
        insights = {
            "BFS": "Optimal for finding shortest path in unweighted graphs",
            "DFS": "Good for exploring all paths or checking connectivity",
            "Binary Search": "Exploits sorted data to achieve logarithmic complexity",
            "Dynamic Programming": "Optimal when problem has overlapping subproblems",
            "Backtracking": "Essential for combinatorial problems",
            "Hash Table": "Provides O(1) lookup for frequent access patterns",
            "Two Pointers": "Efficient for problems with two sequences or boundaries",
        }
        return insights.get(algo, "Algorithm chosen based on problem constraints")
    
    def _get_data_structure_insight(self) -> str:
        """Get data structure insight."""
        code_lower = self.code_content.lower() if self.code_content else ""
        
        if "queue" in code_lower or "deque" in code_lower:
            return "Use queue (FIFO) for BFS and level-order processing"
        elif "stack" in code_lower:
            return "Use stack (LIFO) for DFS and traversal operations"
        elif "dict" in code_lower or "hash" in code_lower:
            return "Use hash maps for O(1) lookups and frequency counting"
        elif "set" in code_lower:
            return "Use sets for O(1) membership testing and deduplication"
        else:
            return "Choose data structures based on access patterns"
    
    def _get_optimization_insight(self) -> str:
        """Get optimization insight."""
        algo = self.algorithm_info.get('algorithm', '').lower()
        
        if 'bfs' in algo or 'dfs' in algo:
            return "Prune search space by marking visited nodes"
        elif 'binary' in algo:
            return "Eliminate half of remaining search space each iteration"
        elif 'dp' in algo or 'dynamic' in algo:
            return "Memoize intermediate results to avoid recomputation"
        elif 'two pointer' in algo:
            return "Move pointers strategically to avoid redundant checks"
        else:
            return "Use appropriate algorithms for optimal complexity"
    
    def validate_python(self) -> bool:
        """Validate that the Python file is syntactically correct."""
        if not self.code_content:
            return False
        
        try:
            ast.parse(self.code_content)
            return True
        except SyntaxError as e:
            print(f"Syntax error in {self.submission_file}: {e}")
            return False
    
    def process(self) -> Tuple[bool, str]:
        """Process the entire folder."""
        status = []
        
        if not self.read_code():
            return False, f"Could not read submission file in {self.folder_name}"
        
        status.append(f"✓ Read submission file")
        
        if not self.extract_function_info():
            return False, f"Could not extract function info from {self.folder_name}"
        
        status.append(f"✓ Extracted function: {self.function_name}")
        
        if not self.add_docstring_to_code():
            return False, f"Could not add docstring to {self.folder_name}"
        
        status.append(f"✓ Added docstring and inline comments")
        
        if not self.validate_python():
            return False, f"Python validation failed for {self.folder_name}"
        
        status.append(f"✓ Validated Python syntax")
        
        if not self.write_code():
            return False, f"Could not write code for {self.folder_name}"
        
        status.append(f"✓ Wrote updated code")
        
        if not self.generate_readme():
            return False, f"Could not generate README for {self.folder_name}"
        
        status.append(f"✓ Generated README.md")
        
        return True, " | ".join(status)


def main():
    """Main function to process all submission folders."""
    
    print("=" * 80)
    print("NEETCODE SUBMISSION DOCUMENTATION GENERATOR")
    print("=" * 80)
    print()
    
    # Get all submission folders
    if not BASE_DIR.exists():
        print(f"Error: Base directory not found: {BASE_DIR}")
        return
    
    folders = sorted([f for f in BASE_DIR.iterdir() if f.is_dir()])
    total_folders = len(folders)
    
    print(f"Found {total_folders} submission folders")
    print(f"Base directory: {BASE_DIR}")
    print()
    
    stats = {
        "total": total_folders,
        "processed": 0,
        "successful": 0,
        "failed": 0,
        "errors": []
    }
    
    print("Processing folders...")
    print("-" * 80)
    
    for idx, folder_path in enumerate(folders, 1):
        folder_name = folder_path.name
        documenter = SubmissionDocumenter(folder_path)
        
        success, message = documenter.process()
        
        if success:
            stats["successful"] += 1
            status_icon = "✓"
            status_color = ""
        else:
            stats["failed"] += 1
            status_icon = "✗"
            status_color = ""
            stats["errors"].append(f"{folder_name}: {message}")
        
        stats["processed"] += 1
        
        # Print progress
        progress = f"[{idx:3d}/{total_folders}] {status_icon} {folder_name:50s}"
        print(f"{progress}")
        
        # Show detailed message if available
        if message and success:
            pass  # Could print details if needed
    
    print("-" * 80)
    print()
    
    # Print summary statistics
    print("=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)
    print(f"Total Folders:     {stats['total']}")
    print(f"Successfully Processed: {stats['successful']}")
    print(f"Failed:            {stats['failed']}")
    print(f"Success Rate:      {100*stats['successful']/stats['total']:.1f}%")
    print()
    
    if stats['errors']:
        print("ERRORS:")
        print("-" * 80)
        for error in stats['errors']:
            print(f"  ✗ {error}")
        print()
    
    print("=" * 80)
    print("Documentation generation complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
