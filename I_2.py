# Convert Conditional to Ternary
(subject === "DSA" && grade >= 80)
  ? console.log("You may enroll Application Development")
  : (subject === "Math101" && grade <= 80)
    ? console.log("You may enroll Calculus")
    : console.log("You have to enroll DSA and pass to enroll AD and Math101 and pass to enroll Calculus");
