'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { useParams } from 'next/navigation';
import AdminSidebar from '@/components/admin/AdminSidebar';
import { useLanguage } from '@/context/LanguageContext';
import { formatPrice } from '@/lib/utils';
import {
  Printer,
  Truck,
  ArrowRight,
  ArrowLeft,
  CheckCircle2,
  Clock,
  MapPin,
  Phone,
  User,
  Package,
} from 'lucide-react';

export default function AdminOrderDetailsPage() {
  const params = useParams();
  const { locale, dir } = useLanguage();
  const orderId = (params?.id as string) || 'MESS-842910';

  const [status, setStatus] = useState<'PENDING' | 'PROCESSING' | 'SHIPPED' | 'DELIVERED'>('SHIPPED');

  const orderData = {
    orderNumber: orderId,
    date: '21 نوفمبر 2026 - 02:15 م',
    customer: {
      name: 'م. أحمد الشناوي',
      company: 'شركة النيل للحلول الرقمية',
      phone: '01012345678',
      governorate: 'القاهرة',
      city: 'القاهرة الجديدة - التجمع الخامس',
      address: 'شارع التسعين الشمالي، مجمع البنوك، مبنى رقم 12',
      notes: 'برجاء الاتصال قبل التوصيل بساعة للتنسيق مع أمن المبنى',
    },
    items: [
      {
        id: '1',
        name: 'سويتش سيسكو كاتاليست 24 بورت PoE+ جيجابت (370W)',
        model: 'C1000-24P-4G-L',
        brand: 'Cisco',
        quantity: 1,
        price: 18480,
      },
      {
        id: '2',
        name: 'أكسس بوينت يوبيكويتي UniFi U6 Pro واي فاي 6 سقف داخلي',
        model: 'U6-Pro',
        brand: 'Ubiquiti',
        quantity: 2,
        price: 8599,
      },
    ],
    subtotal: 35678,
    shippingFee: 0,
    total: 35678,
    paymentMethod: 'الدفع عند الاستلام نقداً (COD)',
  };

  return (
    <div className="flex min-h-screen bg-slate-50">
      <AdminSidebar />

      <main className="flex-1 p-6 sm:p-8 space-y-6 overflow-y-auto">
        {/* Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-5">
          <div className="flex items-center gap-3">
            <Link
              href="/admin/orders"
              className="p-2 rounded-xl border border-slate-200 hover:bg-slate-100 text-slate-700"
            >
              {dir === 'rtl' ? <ArrowRight className="w-4 h-4" /> : <ArrowLeft className="w-4 h-4" />}
            </Link>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-xl sm:text-2xl font-black text-petrol-900 font-mono">{orderId}</h1>
                <span className="px-2.5 py-0.5 rounded-full bg-sky-50 text-sky-700 font-bold text-xs border border-sky-200">
                  {status}
                </span>
              </div>
              <span className="text-xs text-slate-400 font-mono">{orderData.date}</span>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <button
              onClick={() => window.print()}
              className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl border border-slate-300 bg-white hover:bg-slate-50 text-slate-800 font-bold text-xs shadow-xs"
            >
              <Printer className="w-4 h-4" />
              <span>طباعة بوليصة الشحن (Waybill)</span>
            </button>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Order Items & Pricing */}
          <div className="lg:col-span-2 space-y-6">
            <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-subtle space-y-4">
              <h3 className="font-extrabold text-sm text-petrol-900 border-b border-slate-100 pb-3 flex items-center gap-2">
                <Package className="w-4 h-4 text-sky-600" />
                <span>المنتجات المطلوبة ({orderData.items.length})</span>
              </h3>

              <div className="divide-y divide-slate-100 text-xs">
                {orderData.items.map((item) => (
                  <div key={item.id} className="py-3 flex items-center justify-between">
                    <div>
                      <h4 className="font-bold text-petrol-950">{item.name}</h4>
                      <span className="text-slate-400 font-mono">
                        {item.brand} • {item.model} | الكمية: {item.quantity}
                      </span>
                    </div>
                    <span className="font-mono font-black text-petrol-900">
                      {formatPrice(item.price * item.quantity, locale)}
                    </span>
                  </div>
                ))}
              </div>

              {/* Summary */}
              <div className="border-t border-slate-200 pt-3 space-y-2 text-xs">
                <div className="flex justify-between text-slate-600">
                  <span>المجموع الفرعي</span>
                  <span className="font-mono font-bold">{formatPrice(orderData.subtotal, locale)}</span>
                </div>
                <div className="flex justify-between text-slate-600">
                  <span>تكلفة الشحن</span>
                  <span className="font-mono font-bold text-emerald-600">مجاناً (فوق 10,000 ج.م)</span>
                </div>
                <div className="flex justify-between text-base font-black text-petrol-900 border-t border-slate-200 pt-2">
                  <span>المبلغ المطلوب تحصيله (COD)</span>
                  <span className="font-mono text-lg text-petrol-950">{formatPrice(orderData.total, locale)}</span>
                </div>
              </div>
            </div>

            {/* Change Status Card */}
            <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-subtle flex items-center justify-between gap-4">
              <div>
                <h4 className="font-bold text-xs text-petrol-900">تحديث حالة الطلب</h4>
                <p className="text-[11px] text-slate-500">يتغير مسار التتبع فوراً في صفحة العميل</p>
              </div>

              <select
                value={status}
                onChange={(e) => setStatus(e.target.value as any)}
                className="text-xs font-bold px-3 py-2 rounded-xl border border-petrol-300 bg-petrol-50 text-petrol-900 focus:outline-none"
              >
                <option value="PENDING">جديد (قيد المراجعة)</option>
                <option value="PROCESSING">قيد التجهيز في المستودع</option>
                <option value="SHIPPED">خرج مع المندوب للتسليم</option>
                <option value="DELIVERED">تم التسليم والتحصيل</option>
              </select>
            </div>
          </div>

          {/* Customer & Delivery Details */}
          <div className="space-y-6">
            <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-subtle space-y-4">
              <h3 className="font-extrabold text-sm text-petrol-900 border-b border-slate-100 pb-3 flex items-center gap-2">
                <User className="w-4 h-4 text-sky-600" />
                <span>بيانات العميل والشحن</span>
              </h3>

              <div className="space-y-3 text-xs">
                <div>
                  <span className="text-slate-400 block text-[11px]">اسم العميل:</span>
                  <span className="font-bold text-slate-800">{orderData.customer.name}</span>
                  {orderData.customer.company && (
                    <span className="text-[11px] text-sky-700 block">{orderData.customer.company}</span>
                  )}
                </div>

                <div>
                  <span className="text-slate-400 block text-[11px]">رقم الهاتف:</span>
                  <span className="font-mono font-bold text-slate-800">{orderData.customer.phone}</span>
                </div>

                <div>
                  <span className="text-slate-400 block text-[11px]">عنوان التوصيل:</span>
                  <p className="font-medium text-slate-800 leading-relaxed">
                    {orderData.customer.address}
                  </p>
                  <span className="text-[11px] text-slate-500">
                    {orderData.customer.city}، {orderData.customer.governorate}
                  </span>
                </div>

                {orderData.customer.notes && (
                  <div className="p-3 rounded-xl bg-amber-50 border border-amber-100 text-amber-900">
                    <span className="font-bold block text-[10px] mb-0.5">ملاحظات التوصيل:</span>
                    <p className="text-[11px]">{orderData.customer.notes}</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
