import random

class Customer:
   def __init__(self, customer_id, processing_time):
       self.customer_id = customer_id
       self.processing_time = processing_time
       self.wait_time = 0

 

class Teller:
   def __init__(self, teller_id):
       self.teller_id = teller_id
       self.current_customer = None

 

def simulate_bank_token_system(num_customers, num_tellers):
   # Step a: Define necessary data structures
   customers = [Customer(i, random.randint(1, 10)) for i in range(num_customers)]
   tellers = [Teller(i) for i in range(num_tellers)]

 

   # Step b: Initialize simulation
   token_queue = list(range(num_customers))
   time = 0
   total_wait_time = 0

 

   # Step f: Run the simulation
   while token_queue or any(teller.current_customer is not None for teller in tellers):
       # Step c: Generate customer tokens
       if token_queue:
           customer_id = token_queue.pop(0)
           customer = customers[customer_id]
           total_wait_time += customer.wait_time
           print(f"Customer {customer.customer_id} arrived with processing time {customer.processing_time}.")

 

       # Step d: Serve customers
       for teller in tellers:
           if teller.current_customer is None:
               if token_queue:
                   customer_id = token_queue.pop(0)
                   customer = customers[customer_id]
                   teller.current_customer = customer
                   print(f"Teller {teller.teller_id} serving customer {customer.customer_id}.")

 

       # Step e: Track wait times and queue lengths
       for customer in customers:
           if customer not in token_queue and customer not in [teller.current_customer for teller in tellers]:
               customer.wait_time += 1

 

       time += 1

 

       for teller in tellers:
           if teller.current_customer is not None:
               teller.current_customer.processing_time -= 1
               if teller.current_customer.processing_time == 0:
                   print(f"Teller {teller.teller_id} finished serving customer {teller.current_customer.customer_id}.")
                   teller.current_customer = None

 

   # Step g: Output results
   num_customers_served = num_customers
   average_wait_time = total_wait_time / num_customers_served
   print(f"\nSimulation finished.\nTotal customers served: {num_customers_served}\nAverage wait time: {average_wait_time:.2f} units of time.")

 

# Example usage
simulate_bank_token_system(8, 2)

