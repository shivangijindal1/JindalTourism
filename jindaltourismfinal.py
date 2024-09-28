import tkinter as tk
from tkinter import messagebox  # Importing messagebox for popups
from tkinter import PhotoImage

# Simple cart list to store tour items
cart = []

# Free and Paid tour dictionaries and transportation+insurance bookings with prices for paid tours
free_tours = {
    "Dubare Elephant Camp Tour": "Experience the beauty of nature and interact with elephants in their natural habitat.The Dubare Camp, where elephants were trained for the famous Mysore Dasara, found a brand new calling. Today, it’s a place where hundreds of tourists get one-on-one with their biggest (quite literally) dream. The Dubare Elephant Camp is a chance to get to know these giant, enchanting creatures better. With a host of activities built around this, many a guest has left the camp with a sense of responsibility to do their bit towards protecting elephants. A trained naturalist takes our guests through the complexities of elephant history, ecology and biology.",
    "Abbey Falls Tour": "Also known as Abbi Falls, Abbey Falls, located near Madikeri, is a perfect place to visit in Coorg. It is also one of the most sought tourism place with our Coorg honeymoon packages The sight of water falling from a cliff with a height of 70 feet, surrounded by lush greenery is indeed a sight that will behold everyone’s attention. The waterfall is a combination of many streams that come together and fall into a pool of water that flows and merge into River Kaveri. The scenic grandeur of Abbey Falls increases by many folds in monsoon. During Monsoon, the stream of water becomes thicker with louder roar. Adding to it is the richer greenery around, which does create sight of a lifetime.Visit the stunning Abbey Falls and enjoy a picturesque view of the surrounding hills.",
    "Namdroling Monastery Tour": "The Thegchog Namdrol Shedrub Dargye Ling informally known as Namdroling Monastery is the largest teaching center of the Nyingma lineage of Tibetan Buddhism in the world. Located in Bylakuppe, part of the Mysuru district of the state of Karnataka, the monastery is home to a sangha community of more than five thousand monks and nuns and qualified teachers ",
    "Mallalli Waterfalls": "Mallalli Falls is situated in the Somwarpet Coorg District in Karnataka state in south India. The Kumaradhara River is the main watercourse for this waterfall. The Kumaradhara later flows through Kukke Subrahmanya and merges with the Netravati River at Uppinangadi, which then empties into the Arabian Sea at Mangalore."
    }

paid_tours = {
    "Coffee Plantation Tour": (" The first coffee estate was established in Coorg in 1854 by an Englishman named John Fowler. Soon, almost every family in Coorg began to grow the infamous bean that energizes people across the globe. This tradition has been carried through generations to present day, perhaps contributing to the nickname Coorg has acquired of being “the coffee cup of India. \n\n Entry: Rs1000.", 1000),  # price in Rs
    "Adventure Trekking Tour": ("Experience the thrill of trekking in Coorg's scenic landscapes. Dive into hikes tailored to your fitness level, whether you seek adrenaline or just a laid back break from your city life, we've got you!\n\n Entry: Rs1500.", 1500),
    "Wildlife Safari Tour": ("Get up close with Coorg's diverse wildlife. Experience the thrill of seeing animals in the open and wildlife at its best! perfect for a weekend getaway! \n\n Entry: Rs1200.", 1200),
    "Raja's Seat Garden Tour": ("About 1 km west of the Madikeri bus stand is Raja’s Seat. Popular lore claims that Kodava kings their consorts spent their evenings in the fine park here. It is easy to see why: dramatic views of an orange sun dipping behind the mountains can mesmerize both royals and commoners. This point overlooks green mountains and valleys, beribboned with the distant silver of roads and rivers. \n\n Entry: Rs1500. ", 1500)
}

book_trans = {
    "Flight Booking": ("At this moment, we provide the following flights all at a fixed rate of Rs 5000 \n \n 1. Delhi-Mangalore \n 2. Mumbai-Mangalore \n 3. Kolkata-Mangalore \n 4. Chennai-Mangalore \n \n Sorry about any inconveniences caused. We are working hard to bring nationwide connectivity.", 5000),
    "Train Booking": ("At this moment, we provide the following trains all at a fixed rate of Rs 4000 \n \n 1. Delhi-Mangalore \n 2. Mumbai-Mangalore \n 3. Kolkata-Mangalore \n 4. Chennai-Mangalore \n \n Sorry about any inconveniences caused. We are working hard to bring nationwide connectivity.", 4000),
    "Bus Booking": ("At this moment, we provide the following buses all at a fixed rate of Rs 3000 \n \n 1. Delhi-Mangalore \n 2. Mumbai-Mangalore \n 3. Kolkata-Mangalore \n 4. Chennai-Mangalore \n \n Sorry about any inconveniences caused. We are working hard to bring nationwide connectivity.", 5000)
}

book_insu = {
    "Health Insurance": ("Covers everything at just Rs 1000! \n1. Accidental Death \n2. Accidents \n3. ER visits", 1000),
    "Travel Insurance": ("Car was in an accident? We've got you covered at Rs 1000!", 1000)
}
# Function to create a new window for tour information
def show_tour_info(tour_name, tour_info):
    info_window = tk.Toplevel(root)
    info_window.title(tour_name)
    info_window.geometry("1300x800")
    info_window.configure(bg="#C3B1E1")  # Set background color to light purple
    
    # Title label for the tour info window
    tour_title_label = tk.Label(info_window, text=tour_name, height=2, width=30, font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
    tour_title_label.pack(pady=10)

    # Tour information label
    tour_label = tk.Label(info_window, text=tour_info, wraplength=550, bg="#C3B1E1", font=("Arial", 12, "bold"))
    tour_label.pack(pady=20)

    # Button to add to cart
    add_button = tk.Button(info_window, text="Add to Cart", command=lambda: add_to_cart(tour_name), height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    add_button.pack(pady=10)

    # Close button
    close_button = tk.Button(info_window, text="Close", command=info_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="pink")
    close_button.pack(pady=10)
    close_button.place(x=1000, y=550)

    #view cart button
    view_cart_button = tk.Button(info_window, text="View Cart", command=show_cart, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    view_cart_button.pack(pady=5)
    view_cart_button.place(x=20,y=550)
    
# Function to add tour to cart
def add_to_cart(tour_name):
    if tour_name not in cart:  # Prevent adding duplicates
        cart.append(tour_name)
    show_cart()  # Show the updated cart page

# Function to show the cart content and allow checkout
def show_cart():
    cart_window = tk.Toplevel(root)
    cart_window.title("Cart")
    cart_window.geometry("1300x800")
    cart_window.configure(bg="#C3B1E1")  # Set cart window background color

    # Cart items label
    if cart:
        cart_items = "\n".join(cart)
        cart_label = tk.Label(cart_window, text=f"YOUR CART", font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
        cart_label.pack(pady=10)
        cart_label = tk.Label(cart_window, text=f"Items in your cart:\n \n {cart_items}", bg="#C3B1E1", font=("Arial", 14, "bold"))
        cart_label.pack(pady=20)
      
        #checkout button 
        checkout_button = tk.Button(cart_window, text="Checkout", command=show_checkout, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
        checkout_button.pack(pady=10)

    else:
        empty_cart_label = tk.Label(cart_window, text="Your cart is empty!", bg="#C3B1E1", font=("Arial", 14, "bold"))
        empty_cart_label.pack(pady=20)

    #close button
    close_button = tk.Button(cart_window, text="Close", command=cart_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)
    close_button.place(x=20,y=550)

    #back button
    back_button = tk.Button(cart_window, text="Back to Home", command=cart_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="pink")
    back_button.pack(pady=10)
    back_button.place(x=1000,y=550)

# Function to show the checkout page
def show_checkout():
    checkout_window = tk.Toplevel(root)
    checkout_window.title("Checkout")
    checkout_window.geometry("1300x800")
    checkout_window.configure(bg="#C3B1E1")

    checkout_label = tk.Label(checkout_window, text=f"Thank you for stopping by!! see you in Coorg!", font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
    checkout_label.pack(pady=10)

    checkout_label = tk.Label(checkout_window, text="You have selected the following tours and transportation:", font=("Arial", 18, "bold"), bg="#C3B1E1")
    checkout_label.pack(pady=10)

    total_amount = 0  # Initialize total amount
    for tour in cart:
        if tour in free_tours:
            tour_price = 0
            tour_label = tk.Label(checkout_window, text=f"- {tour} (Free)", font=("Arial", 12, "underline"), bg="#C3B1E1")
            tour_label.pack()
        elif tour in paid_tours:
            tour_price = paid_tours[tour][1]  # Get the price of the paid tour
            total_amount += tour_price
            tour_label = tk.Label(checkout_window, text=f"- {tour} (Paid Tour: Rs {tour_price})", font=("Arial", 12, "underline"), bg="#C3B1E1")
            tour_label.pack()
        elif tour in book_trans:
            tour_price = book_trans[tour][1]  # Get the price of the transportation
            total_amount += tour_price
            tour_label = tk.Label(checkout_window, text=f"- {tour} (Transport: Rs {tour_price})", font=("Arial", 12, "underline"), bg="#C3B1E1")
            tour_label.pack()
        elif tour in book_insu:
            tour_price = book_insu[tour][1]
            total_amount += tour_price
            tour_label = tk.Label(checkout_window, text=f"- {tour} (Insurance: Rs {tour_price})", font=("Arial", 12, "underline"), bg="#C3B1E1")
            tour_label.pack()
        
    total_label = tk.Label(checkout_window, text=f"Total Amount to be Paid: Rs {total_amount}", font=("Arial", 14, "bold"), bg="#C3B1E1")
    total_label.pack(pady=10)

    donation_label = tk.Label(checkout_window, text="Would you like to make a donation? ", bg="#C3B1E1", font=("Arial", 12, "bold"))
    donation_label.pack(pady=5)

    donation_entry = tk.Entry(checkout_window)
    donation_entry.pack(pady=5)

    confirm_button = tk.Button(checkout_window, text="Confirm Booking", command=lambda: confirm_booking(donation_entry.get(), total_amount), height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    confirm_button.pack(pady=10)

    close_button = tk.Button(checkout_window, text="Close", command=checkout_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)

# Function to confirm the booking and show confirmation page
def confirm_booking(donation, total_amount):
    booking_details = "\n".join(cart)  # Get the booked tours
    show_confirmation_page(booking_details, donation, total_amount)

# Function to show the booking confirmation page
def show_confirmation_page(booking_details, donation, total_amount):
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Booking Confirmation")
    confirmation_window.geometry("1300x800")
    confirmation_window.configure(bg="#C3B1E1")  # Set background color to light yellow

    confirmation_label = tk.Label(confirmation_window, text="Booking Confirmation", font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
    confirmation_label.pack(pady=10)

    if donation and donation.isdigit():
        donation_amount = int(donation)
        thank_you_message = f"Thank you for your generous donation of Rs {donation_amount}!\n"
    else:
        donation_amount = 0
        thank_you_message = "Thank you!\n"

    details_label = tk.Label(confirmation_window, text=f"{thank_you_message}Details of your booking:\n{booking_details}\nTotal Amount: Rs {total_amount} + {donation_amount}", 
                              wraplength=550, bg="#C3B1E1", font=("Arial", 14, "bold"))
    details_label.pack(pady=20)

    pay_button = tk.Button(confirmation_window, text="Pay Now", command=lambda: confirm_payment(total_amount, donation_amount), height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    pay_button.pack(pady=10)

    close_button = tk.Button(confirmation_window, text="Close", command=confirmation_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)

# Function to handle payment confirmation
def confirm_payment(total_amount, donation_amount):
    messagebox.showinfo("Payment Confirmation", f"Payment of Rs {total_amount + donation_amount} confirmed! Thank you for booking with us!")
    cart.clear()  # Clear the cart after payment
    root.quit()  # Exit the application after payment confirmation

# Function to book transportation
def book_transportation():
    trans_window = tk.Toplevel(root)
    trans_window.title("Book Transportation")
    trans_window.geometry("1300x800")
    trans_window.configure(bg="#C3B1E1")  # Set background color to light yellow

    trans_label = tk.Label(trans_window, text="Choose a mode of transportation:", font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
    trans_label.pack(pady=10)
    
    trans_label = tk.Label(trans_window, text="Book transport with the click of a button!! \n You know what's more exciting than that? \n We provide affordable fix rate transportation!!",font=("Arial", 16, "bold"), bg="#C3B1E1")
    trans_label.pack(pady=10)
    
    trans_label = tk.Label(trans_window, text="At this moment, we only provide transportation from certain destinations. \n Stay tuned for more! \n \n",font=("Arial", 12, "bold"), bg="#C3B1E1")
    trans_label.pack(pady=10)



    # Create buttons for each transportation option
    for trans_name, (trans_info, price) in book_trans.items():
        trans_button = tk.Button(trans_window, text=trans_name, command=lambda name=trans_name: show_trans_info(name), height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
        trans_button.pack(pady=5)

    view_cart_button = tk.Button(trans_window, text="View Cart", command=show_cart, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    view_cart_button.pack(pady=5)
    view_cart_button.place(x=20,y=550)

    back_button = tk.Button(trans_window, text="Back to Home", command=trans_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="pink")
    back_button.pack(pady=5)
    back_button.place(x=1000,y=550)

# Function to show transportation information
def show_trans_info(trans_name):
    trans_info = book_trans[trans_name][0]
    trans_window = tk.Toplevel(root)
    trans_window.title(trans_name)
    trans_window.geometry("1300x800")
    trans_window.configure(bg="#C3B1E1")  # Set background color to light yellow

    # Title label for the transportation info window
    trans_title_label = tk.Label(trans_window, text=trans_name, font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
    trans_title_label.pack(pady=10)

    # Transportation information label
    trans_label = tk.Label(trans_window, text=trans_info, wraplength=550, bg="#C3B1E1", font=("Arial", 12, "bold"))
    trans_label.pack(pady=20)
    
    # Add to cart button
    add_to_cart_button = tk.Button(trans_window, text="Add to Cart", command=lambda: add_to_cart(trans_name), height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    add_to_cart_button.pack(pady=10)

    close_button = tk.Button(trans_window, text="Close", command=trans_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)
    close_button.place(x=20,y=550)

    back_button = tk.Button(trans_window, text="Back to Home", command=trans_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="pink")
    back_button.pack(pady=10)
    back_button.place(x=1000,y=550)

# Function to show free tours
def show_free_tours():
    free_tours_window = tk.Toplevel(root)
    free_tours_window.title("Free Tours")
    free_tours_window.geometry("1300x800")
    free_tours_window.configure(bg="#C3B1E1")  # Set background color to light purple

    # Title label for free tours window
    free_tours_label = tk.Label(free_tours_window, text="Available Free Tours", font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
    free_tours_label.pack(pady=10)

    free_tours_label = tk.Label(free_tours_window, text="\n \n We offer a range of free of cost tours as an initiative to promote tourism in Coorg! \n \n ", font=("Arial", 16, "bold"), bg="pink", fg="black")
    free_tours_label.pack(pady=10)
    # Create buttons for each free tour
    for tour_name, tour_info in free_tours.items():
        tour_button = tk.Button(free_tours_window, text=tour_name, 
                                command=lambda name=tour_name, info=tour_info: show_tour_info(name, info), 
                                height=2, width=30, font=("Arial", 14, "bold"), bg="#FFD700")
        tour_button.pack(pady=10)

    view_cart_button = tk.Button(free_tours_window, text="View Cart", command=show_cart, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    view_cart_button.pack(pady=5)
    view_cart_button.place(x=20,y=550)
    
    back_button = tk.Button(free_tours_window, text="Back to Home", command=free_tours_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="pink")
    back_button.pack(pady=10)
    back_button.place(x=1000,y=550)
    
# Function to show paid tours
def show_paid_tours():
    paid_tours_window = tk.Toplevel(root)
    paid_tours_window.title("Paid Tours")
    paid_tours_window.geometry("1300x800")
    paid_tours_window.configure(bg="#C3B1E1")  # Set background color to light purple

    # Title label for paid tours window
    paid_tours_label = tk.Label(paid_tours_window, text="Available Paid Tours", font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
    paid_tours_label.pack(pady=10)

    paid_tours_label = tk.Label(paid_tours_window, text="\n \n We provide some extraordinary tours at a very low cost as well! \n Happy travels! \n \n", font=("Arial", 14, "bold"), bg="pink", fg="black")
    paid_tours_label.pack(pady=10)

    # Create buttons for each paid tour
    for tour_name, (tour_info, price) in paid_tours.items():
        tour_button = tk.Button(paid_tours_window, text=tour_name, 
                                command=lambda name=tour_name, info=tour_info: show_tour_info(name, info), 
                                height=2, width=30, font=("Arial", 14, "bold"), bg="#FFD700")
        tour_button.pack(pady=10)

    view_cart_button = tk.Button(paid_tours_window, text="View Cart", command=show_cart, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    view_cart_button.pack(pady=5)
    view_cart_button.place(x=20,y=550)

    back_button = tk.Button(paid_tours_window, text="Back to Home", command=paid_tours_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="pink")
    back_button.pack(pady=10)
    back_button.place(x=1000,y=550)

def show_insurance_page():
    insurance_window = tk.Toplevel(root)
    insurance_window.title("Insurance Options")
    insurance_window.geometry("1300x800")
    insurance_window.configure(bg="#C3B1E1")

    title_label = tk.Label(insurance_window, text="Insurance Options", font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
    title_label.pack(pady=10)

    title_label=tk.Label(insurance_window, text=f"We've got you covered under the JTInsurancescheme!! \n Only at Rs 1000!! \n (clicking will add it to cart) \n \n  Health Insurance covers: \n 1. accidental death \n 2. emergency room visits \n 3. over the counter medicines \n \n Travel insurance covers: \n 1. car damages \n 2. accidents \n 3. lost property \n lost passport costs \n", font=("Arial", 16, "bold"), bg="#C3B1E1")
    title_label.pack(pady=10)
    for insurance_name, (info, price) in book_insu.items():
        ins_button = tk.Button(insurance_window, text=insurance_name, command=lambda name=insurance_name: add_insurance_to_cart(name), height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
        ins_button.pack(pady=5)

    close_button = tk.Button(insurance_window, text="Close", command=insurance_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)

    view_cart_button = tk.Button(insurance_window, text="View Cart", command=show_cart, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    view_cart_button.pack(pady=5)
    view_cart_button.place(x=20,y=550)

    back_button = tk.Button(insurance_window, text="Back to Home", command=insurance_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="pink")
    back_button.pack(pady=10)
    back_button.place(x=1000,y=550)
def add_insurance_to_cart(insurance_name):
    if insurance_name not in cart:
        cart.append(insurance_name)
        messagebox.showinfo("Added to Cart", f"{insurance_name} has been added to your cart!")
    else:
        messagebox.showwarning("Already in Cart", f"{insurance_name} is already in your cart.")


# Main application window
root = tk.Tk()
root.title("JindalTourism.net")
root.geometry("1300x800")  # Set window size
root.configure(bg="#C3B1E1")  # Set background color to light purple

# Load an image for the home page (make sure to provide a valid path to your image)
# image = PhotoImage(file="path/to/your/image.png")
# image_label = tk.Label(root, image=image, bg="#C3B1E1")
# image_label.pack(pady=10)
image_path=PhotoImage(file=r"C:\Users\Shivangi\Desktop\logo.png")
bg_image=tk.Label(root,image=image_path)
bg_image.place(relheight=1,relwidth=1)

# Title label
title_label = tk.Label(root, text="Welcome to Jindal Tourism!", font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
title_label.pack(pady=10)

# Introduction label
intro_label = tk.Label(root, text="Book tours and transport at the click of a button!!", bg="#C3B1E1", font=("Arial", 18, "bold"))
intro_label.pack(pady=5)

# Introduction label
intro_label = tk.Label(root, text="Jindal Tourism aims at bringing you tours and travels to the hidden gems of Coorg!\n", bg="#C3B1E1", font=("Arial", 14, "bold"))
intro_label.pack(pady=5)

# Button to show free tours
free_tours_button = tk.Button(root, text="Free Tours", command=show_free_tours, height=1, width=40, font=("Arial", 14, "bold"), bg="#FFD700")
free_tours_button.pack(pady=5)

# Button to show paid tours
paid_tours_button = tk.Button(root, text="Paid Tours", command=show_paid_tours, height=1, width=40, font=("Arial", 14, "bold"), bg="#FFD700")
paid_tours_button.pack(pady=5)

# Button to book transport
book_transport_button = tk.Button(root, text="Book Transportation", command=book_transportation, height=1, width=40, font=("Arial", 14, "bold"), bg="#FFD700")
book_transport_button.pack(pady=5)

buy_insurance_button = tk.Button(root, text="Buy Insurance", command=show_insurance_page, height=1, width=40, font=("Arial", 14, "bold"), bg="#FFD700")
buy_insurance_button.pack(pady=5)

# Button to view cart
view_cart_button = tk.Button(root, text="View Cart", command=show_cart, height=1, width=40, font=("Arial", 14, "bold"), bg="#FFD700")
view_cart_button.pack(pady=5)

# Introduction label
intro_label = tk.Label(root, text="THIS MONTH'S HIDDEN GEM IS: ", bg="#C3B1E1", font=("Lucida Handwriting", 20, "bold", "underline"))
intro_label.pack(pady=5)

# Title label
title_label = tk.Label(root, text="ABBEY FALLS", font=("Lucida Handwriting", 30, "bold"), bg="#C3B1E1", fg="brown")
title_label.pack(pady=10)

# Button to go to 'About Us'
about_us_button = tk.Button(root, text="About Us", command=lambda: show_about_us(), height=2, width=40, font=("Arial", 14, "bold"), bg="Pink")
about_us_button.pack(pady=10)

title_label = tk.Label(root, text="JindalTourism | All Rights Reserves", font=("Times New Roman", 15, "bold"), bg="#C3B1E1", fg="black")
title_label.pack(pady=10)

# Function to show About Us information
def show_about_us():
    about_us_window = tk.Toplevel(root)
    about_us_window.title("About Us")
    about_us_window.geometry("1300x800")
    about_us_window.configure(bg="#C3B1E1")  # Set background color to light purple
    
    about_label = tk.Label(about_us_window, text="About Us", font=("Lucida Handwriting", 34, "bold"), bg="#C3B1E1", fg="brown")
    about_label.pack(pady=10)

    about_text = "Welcome to Jindal Tourism, your premier destination for exploring the enchanting beauty of Coorg! Our mission is to provide unforgettable experiences that showcase the hidden gems of this lush region while making tourism accessible to all. \n \n At Jindal Tourism, we believe that everyone deserves the opportunity to explore  the breathtaking landscapes and rich cultural heritage of Coorg. That’s why we proudly offer a variety of free tours designed to encourage tourism and allow visitors to immerse themselves in the natural splendor of the area. \n \n In addition to our free tours, we offer a selection of paid tours that cater to diverse interests, from adventure seekers to cultural enthusiasts. Each tour is crafted with care, ensuring that every guest has a memorable and enriching experience. \n \n To complement our tour offerings, we also provide affordable travel tickets at fixed rates, making it easy for you to explore Coorg without breaking the bank. Whether you're planning a weekend getaway or a week-long adventure,  Jindal Tourism is here to help you make the most of your travels. \n \n Join us as we embark on a journey to discover the magic of Coorg.  We look forward to welcoming you!"
    about_info_label = tk.Label(about_us_window, text=about_text, wraplength=800, bg="#C3B1E1", font=("Arial", 14))
    about_info_label.pack(pady=20)

    close_button = tk.Button(about_us_window, text="Close", command=about_us_window.destroy, height=2, width=20, font=("Arial", 14, "bold"), bg="#FFD700")
    close_button.pack(pady=10)
    close_button.place(x=1000,y=550)


# Run the application
root.mainloop()

