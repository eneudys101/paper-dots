// This is a comment, and is ignored by the compiler.
// You can test this code by clicking the "Run" button over there ->
// or if you prefer to use your keyboard, you can use the "Ctrl + Enter"
// shortcut.

// This code is editable, feel free to hack it!
// You can always return to the original code by clicking the "Reset" button ->

// This is the main function.
//
/// Three slashes generate docs
fn main() {
    // Statements here are executed when the compiled binary is called.

    // Print text to the console.
    println!("Hello World!");

    // The tutorial said to add this. Now im learning to comment in rust.
    /* apparently C style comments work too */

    println!("I'm not writing what the tutorial says.");

    // Lets keep learning with formatting string
    // the {} are replaced with any argument
    println!("I am {} years old", 28);

    // le me try indexing arguments
    println!("My sibling name and age are: ");
    println!("{0} is {1} years old","Aneldys",23);
    println!("{0} is {1} years old","Emma", 5);
    // this one will be purposely wrong for learning purpuse.
    println!("{0} is {2} years old, wait no he is {1} years old","Emmanuel",3,4);
    
    //name arguments too
    println!(
        "My girlfriends's name is {name} and her is is also {age}",
        name="Kiara",
        age=28,
        );
    // i can print my age in different base
    println!("My age in different base");
    println!("Decimal: {}",28);
    println!("Binary: {:b}",28);
    println!("Octal: {:o}",28);
    println!("hex: {:x}",28);
    println!("HEX: {:X}",28);
    
    // justify the text a given amount
    println!("My age:{age:>10}",age= 28);
    println!("My age:{age:0>10}",age=28);
    println!("My age:{age:2>10}",age=28);
    println!("My age:{age:0<10}",age=28);

    // Rust even checks to make sure the correct number of arguments are used.
    println!("My name is {0}, {1} {0}", "Bond","James");
    // FIXME ^ Add the missing argument: "James"

    // Only types that implement fmt::Display can be formatted with `{}`. User-
    // defined types do not implement fmt::Display by default.

    //#[allow(dead_code)] // disable `dead_code` which warn against unused module
    struct Structure(i32);

    // This will not compile because `Structure` does not implement
    // fmt::Display.
    println!("This struct `{}` won't print...", Structure(3));
    // TODO ^ Try uncommenting this line

    // For Rust 1.58 and above, you can directly capture the argument from a
    // surrounding variable. Just like the above, this will output
    // "    1", 4 white spaces and a "1".
    let number: f64 = 1.0;
    let width: usize = 5;
    println!("{number:>width$}");
}
