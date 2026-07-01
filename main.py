class Fleet_Manager:
    def __init__(self):
        self.Drivers=[]
        self.Shipments=[]
        self.Vehicles=[]
    def add_driver(self,driver):
        self.Drivers.append(driver)
        print(f" the driver with id={driver.driver_id}added sucssefully")
    def add_vehicle(self,new_vehicle):
        self.Vehicles.append(new_vehicle)
        print(f" the vehicle with plate number={new_vehicle.plate_number}added sucssefuly")
    def add_shipment(self,new_shipment):
        self.Shipments.append(new_shipment)
        print(f" the shipment with id={new_shipment.shipment_id}added sucssefully")
    def dispatch_shipment(self,Shipment_Object):
    
        for n in self.Vehicles:
            if n.current_driver==None:
                print(f" the vehicle {n.plate_number}no driver available")
                continue
            if n.current_driver.is_available==False:
                print(f"  vehicle {n.plate_number}driver {n.current_driver.name}is unavailable")
                continue
            if n.current_driver.license_type!=n.required_license:
                print(f" the drivers license{n.current_driver.name} does not match the required vehicle{n.plate_number}license catagory")
                continue
            if isinstance(n,Gas_Truck):
                if Shipment_Object.distance>n.fuel_level:
                    print(f"there is not enough fuel in vehicle{n.plate_number} to complete the trip")
                    continue
            if isinstance(n,Electric_Truck):
                if Shipment_Object.distance>n.battery_level:
                    print(f"there is not enough fuel in vehicle{n.plate_number} to complete the trip")
                    continue

            total=0
            for s in n.Shipment:
                total+=s.weight
            if total+Shipment_Object.weight>n.max_capacity:
                print(f" vehicle{n.plate_number}Weight exceeds max capacity")
                continue
                 
            n.Load_Shipment(Shipment_Object)
            n.current_driver.assign_to_trip()
            if isinstance(n,Gas_Truck):
                n.fuel_level-=Shipment_Object.distance
            elif isinstance(n,Electric_Truck):
                n.battery_level-=Shipment_Object.distance
            print(f" has been upload sucssefully {Shipment_Object.shipment_id} and its driver {n.current_driver.name}")
            break
    def complete_delivery(self,vehicle_plate):
        for n in self.Vehicles:
            if n.plate_number==vehicle_plate:
                if n.current_driver!=None:
                    for m in n.Shipment:
                        m.update_status('delivered')
                    n.Shipment=[]
                    n.current_driver.complete_trip()
                break  
        else:
            raise ValueError('the vehicle does not exist')
             
                
                
class Driver:
    def __init__(self,name,driver_id,license_type,is_available=True):
        self.name=name
        self.driver_id=driver_id
        self.license_type=license_type
        self.is_available=is_available
    def assign_to_trip(self):
        self.is_available=False
    def complete_trip(self):
        self.is_available=True
class Shipment:
    def __init__(self,shipment_id,weight,destination,distance,status='pending'):
        self.shipment_id=shipment_id
        self.weight=weight
        self.destination=destination
        self.distance=distance
        self.status=status
    def update_status(self,new_status):
        self.status=new_status
class Vehicle:
    def __init__(self,plate_number,max_capacity,required_license='Heavy'):
        self.plate_number=plate_number
        self.max_capacity=max_capacity
        self.required_license=required_license
        self.current_driver=None
        self.Shipment=[]
    def Assign_Driver(self,driver_object):
        if driver_object.is_available==True:
            self.current_driver=driver_object
            
        else:
            raise ValueError('the driver is not available')
    def Load_Shipment(self,Shipment_Object):
        total_weight=0
        for s in self.Shipment:
            total_weight+=s.weight
        if(total_weight+Shipment_Object.weight<=self.max_capacity):
            self.Shipment.append(Shipment_Object)
            Shipment_Object.update_status(' in transit')
        else:
            raise ValueError('insufficient remaining capacity for the size')
    
        
        
class Gas_Truck(Vehicle):
    def __init__(self,plate_number,max_capacity,fuel_tank_capacity,required_license='heavy'):
        super().__init__(plate_number,max_capacity,required_license)
        self.fuel_tank_capacity=fuel_tank_capacity
        self.fuel_level=fuel_tank_capacity
    def Refuel(self,fuel_amount):
        if fuel_amount<0:
            raise ValueError('the value is not correct')
        if self.fuel_level+fuel_amount>self.fuel_tank_capacity:
            raise ValueError('insufficient remaining capacity for the size')
        else:
            self.fuel_level+=fuel_amount
class Electric_Truck(Vehicle):
    def __init__(self,plate_number,max_capacity,battery_capacity,required_license='heavy'):
        super().__init__(plate_number,max_capacity,required_license)
        self.battery_capacity=battery_capacity
        self.battery_level=battery_capacity
    def Recharge(self,charge_amount):
        if charge_amount<0:
            raise ValueError('enter correct value')
        if charge_amount+self.battery_level>self.battery_capacity:
            raise ValueError('insufficient remaining capacity for the size')
        else:
            self.battery_level+=charge_amount
            
            
            
            
            
            
            
            
manger=Fleet_Manager()
driver_1=Driver('Majd',2020987721,'heavy')
driver_2=Driver('Ahmad',2020950321,'light')
manger.add_driver(driver_1)
manger.add_driver(driver_2)
truck_gas=Gas_Truck('gas_111',1000,100,'heavy')
truck_elec=Electric_Truck('elec_222',300,80,'light')
manger.add_vehicle(truck_gas)
manger.add_vehicle(truck_elec)
truck_gas.Assign_Driver(driver_1)
truck_elec.Assign_Driver(driver_2)
Shipment_1=Shipment('sh_001',600,'aqaba',50)
print('Attempting to load aheavy cargo')
manger.dispatch_shipment(Shipment_1)
Shipment_2=Shipment('sh_002',100,'amman',10)
print('Attempting to load and majd busy')
manger.dispatch_shipment(Shipment_2)
print('finish first trip and order delivred succssefully')
manger.complete_delivery('gas_111')
manger.dispatch_shipment(Shipment_2)




            
