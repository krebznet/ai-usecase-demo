
interface VehicleData {
  id?: string;
  [key: string]: any;
}

class VehicleModel {
  private static data: VehicleData[] = [];
  private static nextId = 1;

  static async create(data: VehicleData): Promise<VehicleData> {
    const newRecord = {
      id: this.nextId.toString(),
      ...data,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };
    
    this.data.push(newRecord);
    this.nextId++;
    
    return newRecord;
  }

  static async findById(id: string): Promise<VehicleData | undefined> {
    return this.data.find(record => record.id === id);
  }

  static async findAll(): Promise<VehicleData[]> {
    return this.data;
  }

  static async update(id: string, updateData: Partial<VehicleData>): Promise<VehicleData | null> {
    const recordIndex = this.data.findIndex(record => record.id === id);
    if (recordIndex === -1) return null;

    this.data[recordIndex] = {
      ...this.data[recordIndex],
      ...updateData,
      updatedAt: new Date().toISOString()
    };

    return this.data[recordIndex];
  }

  static async delete(id: string): Promise<boolean> {
    const recordIndex = this.data.findIndex(record => record.id === id);
    if (recordIndex === -1) return false;

    this.data.splice(recordIndex, 1);
    return true;
  }
}

export { VehicleModel };
