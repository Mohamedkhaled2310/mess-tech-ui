'use client';

import React, { useState } from 'react';
import AdminSidebar from '@/components/admin/AdminSidebar';
import { useLanguage } from '@/context/LanguageContext';
import { formatPrice } from '@/lib/utils';
import { Users, Search, Phone, Mail, MapPin, Eye, ShoppingBag } from 'lucide-react';

interface CustomerItem {
  id: string;
  name: string;
  company?: string;
  phone: string;
  email: string;
  city: string;
  totalOrders: number;
  totalSpent: number;
  lastOrderDate: string;
}

const mockCustomersList: CustomerItem[] = [
  {
    id: 'c-1',
    name: 'م. أحمد الشناوي',
    company: 'شركة النيل للحلول الرقمية',
    phone: '01012345678',
    email: 'ahmed@nile-digital.com',
    city: 'القاهرة (التجمع الخامس)',
    totalOrders: 6,
    totalSpent: 142500,
    lastOrderDate: '21 نوفمبر 2026',
  },
  {
    id: 'c-2',
    name: 'د. كريم فهمي',
    company: 'عيادات النخبة للأسنان',
    phone: '01198765432',
    email: 'dr.karim@elite.med',
    city: 'الجيزة (الدقي)',
    totalOrders: 3,
    totalSpent: 48900,
    lastOrderDate: '21 نوفمبر 2026',
  },
  {
    id: 'c-3',
    name: 'محمود عبد العزيز',
    phone: '01234567890',
    email: 'm.abdelaziz@gmail.com',
    city: 'الإسكندرية (سموحة)',
    totalOrders: 2,
    totalSpent: 24380,
    lastOrderDate: '21 نوفمبر 2026',
  },
  {
    id: 'c-4',
    name: 'م. حسام الدين حسن',
    company: 'دلتا سيستمز للشبكات',
    phone: '01055554433',
    email: 'hossam@delta-net.eg',
    city: 'الدقهلية (المنصورة)',
    totalOrders: 8,
    totalSpent: 215000,
    lastOrderDate: '20 نوفمبر 2026',
  },
];

export default function AdminCustomersPage() {
  const { locale } = useLanguage();
  const [search, setSearch] = useState('');

  const filtered = mockCustomersList.filter(
    (c) =>
      c.name.includes(search) ||
      c.phone.includes(search) ||
      (c.company && c.company.includes(search))
  );

  return (
    <div className="flex min-h-screen bg-slate-50">
      <AdminSidebar />

      <main className="flex-1 p-6 sm:p-8 space-y-6 overflow-y-auto">
        {/* Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-5">
          <div>
            <h1 className="text-2xl font-black text-petrol-900">إدارة العملاء والشركات</h1>
            <p className="text-xs text-slate-500 mt-0.5">
              بيانات التواصل وسجل المشتريات لعملاء ميس تك
            </p>
          </div>
        </div>

        {/* Search */}
        <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-subtle flex items-center justify-between gap-4">
          <div className="relative w-full sm:w-80">
            <Search className="w-4 h-4 text-slate-400 absolute top-1/2 -translate-y-1/2 start-3" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="بحث بالاسم، رقم الهاتف، أو اسم الشركة..."
              className="w-full ps-9 pe-4 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500"
            />
          </div>

          <span className="text-xs text-slate-500 font-mono">
            عدد العملاء: {filtered.length}
          </span>
        </div>

        {/* Customers Table */}
        <div className="bg-white rounded-2xl border border-slate-200 shadow-subtle overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-xs">
              <thead className="bg-slate-50 border-b border-slate-200 text-slate-600 font-bold">
                <tr>
                  <th className="p-3.5 text-start">العميل</th>
                  <th className="p-3.5 text-start">بيانات الاتصال</th>
                  <th className="p-3.5 text-start">المدينة</th>
                  <th className="p-3.5 text-start">عدد الطلبات</th>
                  <th className="p-3.5 text-start">إجمالي المشتريات</th>
                  <th className="p-3.5 text-start">آخر طلب</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {filtered.map((c) => (
                  <tr key={c.id} className="hover:bg-slate-50/70 transition-colors">
                    <td className="p-3.5">
                      <div className="flex items-center gap-2.5">
                        <div className="w-8 h-8 rounded-full bg-petrol-100 text-petrol-800 font-bold flex items-center justify-center shrink-0">
                          {c.name.charAt(0)}
                        </div>
                        <div>
                          <span className="font-bold text-petrol-900 block leading-tight">{c.name}</span>
                          {c.company && (
                            <span className="text-[11px] text-slate-400 font-medium">{c.company}</span>
                          )}
                        </div>
                      </div>
                    </td>
                    <td className="p-3.5 font-mono">
                      <span className="font-bold text-slate-800 block">{c.phone}</span>
                      <span className="text-[11px] text-slate-400">{c.email}</span>
                    </td>
                    <td className="p-3.5 text-slate-700">{c.city}</td>
                    <td className="p-3.5 font-mono font-bold text-petrol-700">
                      {c.totalOrders} طلبات
                    </td>
                    <td className="p-3.5 font-mono font-black text-petrol-950">
                      {formatPrice(c.totalSpent, locale)}
                    </td>
                    <td className="p-3.5 text-slate-500 font-medium">{c.lastOrderDate}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  );
}
