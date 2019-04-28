from I2C import I2C
from constants import *
##from Integral import Integration
from time import time
##from GyroLowHigh import LowPassfilter as LP


class AltIMUv3(I2C):

    # Output registers used by the accelerometer
    accel_registers = [
        LSM303D.OUT_X_L_A,
        LSM303D.OUT_X_H_A,
        LSM303D.OUT_Y_L_A,
        LSM303D.OUT_Y_H_A,
        LSM303D.OUT_Z_L_A,
        LSM303D.OUT_Z_H_A,
    ]

    # Output registers used by the accelerometer
    gyro_registers = [
        L3GD20H.OUT_X_L,
        L3GD20H.OUT_X_H,
        L3GD20H.OUT_Y_L,
        L3GD20H.OUT_Y_H,
        L3GD20H.OUT_Z_L,
        L3GD20H.OUT_Z_H,
    ]

    def __init__(self, bus_id=1):
        """ 
        Set up I2C connection and initialize some flags and values.
        """

        super(AltIMUv3, self).__init__(bus_id)
        self.is_accel_enabled = False
        self.is_gyro_enabled = False
        
##        self.Integreichon = Integration()
##        self.LPf = LP(self.get_accelerometer_cal(),0.8)
        
        

    def __del__(self):
        """ 
        Clean up.
        """
        try:
            # Power down MEMS
            self.write_register(LSM303D_Address, LSM303D.CTRL1, 0x00)
            self.write_register(L3GD20H_Address, L3GD20H.CTRL1, 0x00)
            
            super(AltIMUv3, self).__del__()
        except:
            pass

    def enable(self, accelerometer=True, gyroscope=True):
        if accelerometer:
            self.write_register(LSM303D_Address, LSM303D.CTRL1, 0xA7)
            self.write_register(LSM303D_Address, LSM303D.CTRL2, 0x00)
            
            self.is_accel_enabled = True

        if gyroscope:
            self.write_register(L3GD20H_Address, L3GD20H.CTRL1, 0xEF)
            self.write_register(L3GD20H_Address, L3GD20H.CTRL4, 0x10)
            self.is_gyro_enabled = True

    def get_accelerometer_raw(self):
        """
        Return a 3D vector of raw accelerometer data.
        """

        # Check if accelerometer has been enabled
        if not self.is_accel_enabled:
            raise(Exception('Accelerometer is not enabled!'))

        return self.read_sensor(LSM303D_Address, self.accel_registers)

    def get_gyroscope_raw(self):
        """
        Return a 3D vector of raw gyroscope data.
        """

        # Check if gyrscope has been enabled
        if not self.is_gyro_enabled:
            raise(Exception('Gyroscope is not enabled!'))

        return self.read_sensor(L3GD20H_Address, self.gyro_registers)


    def get_accelerometer_cal(self):
        """
        Return a 3D vector of calibrated accelerometer data.
        """
        raw = self.get_accelerometer_raw()
        scaling = 0.061 / 1000

        cal_x = raw[0] * scaling
        cal_y = raw[1] * scaling
        cal_z = raw[2] * scaling
        #print(round(cal_x,3))

        return [cal_x, cal_y, cal_z]


    def get_integration(self,LPf,Integreichon, samples = 20):
##        Integreichon = self.Integreichon
##        LPf = self.LPf
        equis = []
        lle = []
        ceta = []
        Timing = time()
        for i in range(samples):
            heysha = LPf.update_measurement(self.get_accelerometer_cal())
            equis.append(heysha[0])
            lle.append(heysha[1])
            ceta.append(heysha[2])
        Timing = (time()-Timing)/samples
        #print(Timing)

        return [Integreichon.definite_integral(equis,TimeFactor=Timing),Integreichon.definite_integral(lle,TimeFactor=Timing),Integreichon.definite_integral(ceta,TimeFactor=Timing)]


    def get_accelerometer_average(self,Filter=None, average=3, Posichon=None):
        
        x = []
        y = []
        z = []
        if Filter != None:
            for i in range(average):
                accel = Filter.update_measurement(self.get_accelerometer_cal())
                x.append(accel[0])
                y.append(accel[1])
                z.append(accel[2])
                
            aveX = sum(x)/average
            aveY = sum(y)/average
            aveZ = sum(z)/average
            

        elif Posichon != None:
            aveX = sum(Posichon[0])/average
            aveY = sum(Posichon[1])/average
            aveZ = sum(Posichon[2])/average
        
        else:
            for i in range(average):
                accel =     self.get_accelerometer_cal()
                x.append(accel[0])
                y.append(accel[1])
                z.append(accel[2])
                print([accel[0],accel[1],accel[2]])
            aveX = sum(x)/average
            aveY = sum(y)/average
            aveZ = sum(z)/average
        
        
        
        return [aveX,aveY,aveZ]
        


    def get_gyroscope_cal(self):
        """
        Return a 3D vector of calibrated gyroscope data.
        """
        raw = self.get_gyroscope_raw()
        #scaling = 0.061 / 1000

        cal_x = raw[0] #* scaling
        cal_y = raw[1] #* scaling
        cal_z = raw[2] #* scaling

        return [cal_x, cal_y, cal_z]
