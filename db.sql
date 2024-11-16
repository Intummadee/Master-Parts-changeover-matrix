-- สร้างฐานข้อมูล
CREATE DATABASE WarehouseQueueSystem;

-- ใช้งานฐานข้อมูล
USE WarehouseQueueSystem;

-- ตารางสำหรับข้อมูลรถ (Vehicles)
CREATE TABLE Vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_type ENUM('10 ล้อ', '6 ล้อ', 'กระบะ') NOT NULL,
    license VARCHAR(50) NOT NULL UNIQUE,
);

-- Gate
CREATE TABLE Gate (
    gateId INT AUTO_INCREMENT PRIMARY KEY,
    gateType ENUM('ประเภท 1', 'ประเภท 2', 'ประเภท 3') NOT NULL,
    current_queue_number INT DEFAULT NULL COMMENT 'คิวปัจจุบันที่กำลังให้บริการ',
    is_active BOOLEAN NOT NULL DEFAULT TRUE COMMENT 'สถานะของประตู: 1 = ใช้งานอยู่, 0 = สถานะว่างอยู่',
    next_queue_number INT DEFAULT NULL COMMENT 'คิวถัดไปที่จะให้บริการ'
);

-- ตารางสำหรับข้อมูลคิว (Queues)
CREATE TABLE Queue (
    queueId INT AUTO_INCREMENT PRIMARY KEY,
    queue_number INT NOT NULL ,
    gateId INT NOT NULL ,
    vehicleId INT NOT NULL ,
    queue_time DATETIME NOT NULL ,
    status ENUM('รอ', 'กำลังโหลด', 'เสร็จสิ้น', 'ยกเลิก') NOT NULL DEFAULT 'รอ' ,
    load_start_time DATETIME DEFAULT NULL COMMENT 'เวลาเริ่มการโหลดสินค้า',
    load_end_time DATETIME DEFAULT NULL COMMENT 'เวลาสิ้นสุดการโหลดสินค้า',
    FOREIGN KEY (gateId) REFERENCES Gate(gateId) ON DELETE CASCADE,
    FOREIGN KEY (vehicleId) REFERENCES Vehicles(vehicle_id) ON DELETE CASCADE
);


CREATE TABLE QueueHistory (
    historyId INT AUTO_INCREMENT PRIMARY KEY,
    queueId INT NOT NULL ,
    date DATE NOT NULL COMMENT 'วันที่ของการบันทึกประวัติ',
    loading_duration INT NOT NULL COMMENT 'ระยะเวลาในการโหลดสินค้า',
    FOREIGN KEY (queueId) REFERENCES Queue(queueId) ON DELETE CASCADE
);

CREATE TABLE QueueNotifications (
    notificationID INT AUTO_INCREMENT PRIMARY KEY ,
    notificationTime DATETIME NOT NULL COMMENT 'เวลาที่เกิดการแจ้งเตือน',
    queueId INT NOT NULL COMMENT 'รหัสคิวที่เกี่ยวข้อง',
    notificationMessage TEXT NOT NULL,
    notificationStatus ENUM('ส่งแล้ว', 'ไม่สำเร็จ') DEFAULT 'ส่งแล้ว' ,
    FOREIGN KEY (queueId) REFERENCES Queue(queueId) ON DELETE CASCADE
);