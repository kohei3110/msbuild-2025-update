/**
 * A simple greeting function to demonstrate TypeScript functionality.
 * @param name The name to greet
 * @returns A greeting message
 */
function greet(name: string): string {
  return `Hello, ${name}!`;
}

/**
 * Main execution function
 */
function main(): void {
  console.log(greet("GitHub Copilot"));
  
  // Demonstrate TypeScript features
  const numbers: number[] = [1, 2, 3, 4, 5];
  const sum = numbers.reduce((acc, current) => acc + current, 0);
  
  console.log(`Sum of numbers: ${sum}`);
}

// Execute the main function
main();