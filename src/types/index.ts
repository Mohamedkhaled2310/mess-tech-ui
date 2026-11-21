export type Locale = 'ar' | 'en';
export type Direction = 'rtl' | 'ltr';

export interface Product {
  id: string;
  slug: string;
  name: {
    ar: string;
    en: string;
  };
  brand: string;
  model: string;
  category: 'switches' | 'wifi' | 'storage' | 'ups' | 'attendance' | 'screens' | 'voip' | 'passive';
  price: number;
  oldPrice?: number;
  discountPercent?: number;
  image: string;
  gallery?: string[];
  inStock: boolean;
  stockCount?: number;
  isHot?: boolean;
  isFeatured?: boolean;
  rating: number;
  reviewsCount: number;
  specs: {
    key: { ar: string; en: string };
    value: { ar: string; en: string };
  }[];
  brief: {
    ar: string;
    en: string;
  };
}

export interface CartItem {
  product: Product;
  quantity: number;
}

export interface OrderCustomer {
  fullName: string;
  phone: string;
  governorate: string;
  city: string;
  address: string;
  notes?: string;
}

export interface Order {
  id: string;
  orderNumber: string;
  createdAt: string;
  customer: OrderCustomer;
  items: CartItem[];
  subtotal: number;
  shippingFee: number;
  total: number;
  paymentMethod: 'COD' | 'INSTAPAY' | 'VODAFONE_CASH';
  status: 'PENDING' | 'PROCESSING' | 'SHIPPED' | 'DELIVERED' | 'CANCELLED';
  trackingSteps: {
    title: { ar: string; en: string };
    date?: string;
    completed: boolean;
    current?: boolean;
  }[];
}

export interface FilterState {
  category?: string;
  brand?: string[];
  minPrice?: number;
  maxPrice?: number;
  inStockOnly?: boolean;
  sortBy?: 'featured' | 'price-asc' | 'price-desc' | 'rating';
  query?: string;
}
