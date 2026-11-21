'use client';

import React from 'react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { formatPrice } from '@/lib/utils';
import { ShoppingBag, Truck, FileText, ArrowLeft, ArrowRight, CheckCircle2, Clock } from 'lucide-react';

const mockPastOrders = [
  {
    orderNumber: 'MESS-842910',
    date: '21 نوفمبر 2026',
    status: 'SHIPPED',
    statusText: 'خرج مع مندوب التوصيل',
    statusColor: 'bg-sky-50 text-sky-700 border-sky-200',
    total: 35678,
    items: [
      { name: 'Cisco Catalyst 1000 24-Port PoE+ Switch', count: 1, price: 18480 },
      { name: 'Ubiquiti UniFi U6 Pro Access Point', count: 2, price: 17198 },
    ],
  },
  {
    orderNumber: 'MESS-731902',
    date: '14 أكتوبر 2026',
    status: 'DELIVERED',
    statusText: 'تم التسليم بنجاح',
    statusColor: 'bg-emerald-50 text-emerald-700 border-emerald-200',
    total: 27940,
    items: [
      { name: 'Synology DiskStation DS923+ 4-Bay NAS', count: 1, price: 27940 },
    ],
  },
  {
    orderNumber: 'MESS-619280',
    date: '02 أغسطس 2026',
    status: 'DELIVERED',
    statusText: 'تم التسليم بنجاح',
    statusColor: 'bg-emerald-50 text-emerald-700 border-emerald-200',
    total: 6900,
    items: [
      { name: 'D-Link Cat6 UTP 305M Solid Pure Copper Cable', count: 2, price: 6900 },
    ],
  },
];

export default function CustomerOrdersPage() {
  const { locale, dir } = useLanguage();

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-4">
        <div>
          <nav className="text-xs text-slate-500 mb-1 flex items-center gap-1.5">
            <Link href="/account/profile" className="hover:text-petrol-700">حسابي</Link>
            <span>/</span>
            <span className="text-petrol-900 font-bold">سجل الطلبات</span>
          </nav>
          <h1 className="text-2xl font-black text-petrol-900">سجل طلباتي السابقة</h1>
        </div>

        <Link
          href="/catalog"
          className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-petrol-700 text-white font-bold text-xs"
        >
          <span>تسوق أجهزة جديدة</span>
          {dir === 'rtl' ? <ArrowLeft className="w-3.5 h-3.5" /> : <ArrowRight className="w-3.5 h-3.5" />}
        </Link>
      </div>

      <div className="space-y-4">
        {mockPastOrders.map((ord) => (
          <div
            key={ord.orderNumber}
            className="bg-white rounded-2xl border border-slate-200 shadow-subtle p-5 sm:p-6 space-y-4"
          >
            {/* Header */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-3">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-petrol-50 text-petrol-800 flex items-center justify-center">
                  <ShoppingBag className="w-5 h-5" />
                </div>
                <div>
                  <span className="text-xs text-slate-400 font-mono block">رقم الطلب</span>
                  <span className="font-bold text-sm text-petrol-900 font-mono">{ord.orderNumber}</span>
                </div>
              </div>

              <div className="flex items-center gap-3">
                <span className="text-xs text-slate-400 font-medium">{ord.date}</span>
                <span className={`px-3 py-1 rounded-full text-xs font-bold border ${ord.statusColor}`}>
                  {ord.statusText}
                </span>
              </div>
            </div>

            {/* Items */}
            <div className="divide-y divide-slate-100 text-xs">
              {ord.items.map((it, idx) => (
                <div key={idx} className="py-2.5 first:pt-0 flex items-center justify-between">
                  <div>
                    <h4 className="font-bold text-slate-800">{it.name}</h4>
                    <span className="text-slate-400 font-mono">الكمية: {it.count}</span>
                  </div>
                  <span className="font-mono font-bold text-petrol-900">
                    {formatPrice(it.price, locale)}
                  </span>
                </div>
              ))}
            </div>

            {/* Footer Total & Actions */}
            <div className="border-t border-slate-100 pt-3 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div className="flex items-baseline gap-2">
                <span className="text-xs text-slate-500 font-medium">الإجمالي:</span>
                <span className="text-base font-black text-petrol-900 font-mono">
                  {formatPrice(ord.total, locale)}
                </span>
                <span className="text-[11px] text-slate-400">(شامل الضريبة والشحن)</span>
              </div>

              <div className="flex items-center gap-2">
                <Link
                  href={`/track-order?order=${ord.orderNumber}`}
                  className="px-4 py-2 rounded-xl bg-petrol-50 text-petrol-800 hover:bg-petrol-100 font-bold text-xs flex items-center gap-1.5 transition-colors"
                >
                  <Truck className="w-3.5 h-3.5" />
                  <span>تتبع مسار الشحنة</span>
                </Link>
                <button
                  onClick={() => alert(`طباعة فاتورة الطلب ${ord.orderNumber}`)}
                  className="px-3.5 py-2 rounded-xl border border-slate-200 text-slate-700 hover:bg-slate-50 font-bold text-xs flex items-center gap-1.5"
                >
                  <FileText className="w-3.5 h-3.5" />
                  <span>الفاتورة</span>
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
