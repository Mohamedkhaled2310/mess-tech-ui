'use client';

import React from 'react';
import Link from 'next/link';
import AdminSidebar from '@/components/admin/AdminSidebar';
import { useLanguage } from '@/context/LanguageContext';
import { formatPrice } from '@/lib/utils';
import {
  TrendingUp,
  ShoppingBag,
  Clock,
  AlertTriangle,
  ArrowUpRight,
  Package,
  CheckCircle2,
} from 'lucide-react';

export default function AdminDashboardPage() {
  const { locale } = useLanguage();

  const stats = [
    {
      title: 'إجمالي مبيعات الشهر',
      value: formatPrice(482950, locale),
      trend: '+18.4% عن الشهر السابق',
      icon: <TrendingUp className="w-6 h-6 text-emerald-600" />,
      bg: 'bg-emerald-50 border-emerald-100',
    },
    {
      title: 'طلبات اليوم الجديدة',
      value: '28 طلب',
      trend: '14 بحاجة لمراجعة وتأكيد',
      icon: <ShoppingBag className="w-6 h-6 text-sky-600" />,
      bg: 'bg-sky-50 border-sky-100',
    },
    {
      title: 'طلبات قيد الشحن (COD)',
      value: '42 شحنة',
      trend: 'مع مناديب المحافظات',
      icon: <Clock className="w-6 h-6 text-indigo-600" />,
      bg: 'bg-indigo-50 border-indigo-100',
    },
    {
      title: 'نواقص المخزون والتنبيهات',
      value: '3 أجهزة',
      trend: 'سويتشات كاتاليست قريبة من النفاد',
      icon: <AlertTriangle className="w-6 h-6 text-amber-600" />,
      bg: 'bg-amber-50 border-amber-100',
    },
  ];

  return (
    <div className="flex min-h-screen bg-slate-50">
      <AdminSidebar />

      <main className="flex-1 p-6 sm:p-8 space-y-8 overflow-y-auto">
        {/* Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-5">
          <div>
            <h1 className="text-2xl font-black text-petrol-900">لوحة الإحصائيات العامة</h1>
            <p className="text-xs text-slate-500 mt-0.5">
              متابعة تدفق الطلبات والمبيعات لشبكات وتجهيزات ميس تك في مصر
            </p>
          </div>

          <div className="flex items-center gap-2">
            <Link
              href="/admin/orders"
              className="px-4 py-2 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-bold text-xs shadow-xs"
            >
              جدول إدارة الطلبات &rarr;
            </Link>
          </div>
        </div>

        {/* 4 Stats Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          {stats.map((st, idx) => (
            <div
              key={idx}
              className={`p-5 rounded-2xl border ${st.bg} bg-white shadow-subtle space-y-2`}
            >
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold text-slate-500">{st.title}</span>
                <div className="p-2 rounded-xl bg-slate-50">{st.icon}</div>
              </div>
              <div className="text-2xl font-black text-petrol-950 font-mono">{st.value}</div>
              <span className="text-[11px] font-medium text-emerald-700 block">{st.trend}</span>
            </div>
          ))}
        </div>

        {/* Quick Tables Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Recent Orders Overview */}
          <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-subtle space-y-4">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <h3 className="font-extrabold text-sm text-petrol-900">أحدث الطلبات الواردة</h3>
              <Link href="/admin/orders" className="text-xs font-bold text-sky-700 hover:underline">
                عرض الكل
              </Link>
            </div>

            <div className="space-y-3 text-xs">
              {[
                { id: 'MESS-842910', customer: 'م. أحمد الشناوي', total: 35678, status: 'خرج للشحن' },
                { id: 'MESS-842911', customer: 'د. كريم فهمي', total: 27940, status: 'قيد التجهيز' },
                { id: 'MESS-842912', customer: 'محمود عبد العزيز', total: 18480, status: 'جديد' },
              ].map((ord) => (
                <div
                  key={ord.id}
                  className="p-3 rounded-xl bg-slate-50/70 border border-slate-100 flex items-center justify-between"
                >
                  <div>
                    <span className="font-mono font-bold text-petrol-900 block">{ord.id}</span>
                    <span className="text-slate-500 text-[11px]">{ord.customer}</span>
                  </div>
                  <div className="text-end">
                    <span className="font-mono font-bold text-petrol-950 block">
                      {formatPrice(ord.total, locale)}
                    </span>
                    <span className="text-[10px] font-bold text-sky-700">{ord.status}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Low Stock Alerts */}
          <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-subtle space-y-4">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <h3 className="font-extrabold text-sm text-petrol-900">تنبيهات المخزون الحرج</h3>
              <Link href="/admin/products" className="text-xs font-bold text-sky-700 hover:underline">
                إدارة المخزون
              </Link>
            </div>

            <div className="space-y-3 text-xs">
              {[
                { name: 'Huawei IdeaHub 65" 4K Smart Screen', left: '3 قطع فقط', brand: 'Huawei' },
                { name: 'Synology DS923+ 4-Bay NAS', left: '8 قطع فقط', brand: 'Synology' },
                { name: 'APC Smart-UPS 1500VA Tower', left: '11 قطعة', brand: 'APC' },
              ].map((item, idx) => (
                <div
                  key={idx}
                  className="p-3 rounded-xl bg-amber-50/50 border border-amber-100 flex items-center justify-between"
                >
                  <div>
                    <span className="font-bold text-petrol-900 block">{item.name}</span>
                    <span className="text-slate-400 text-[10px] font-mono">{item.brand}</span>
                  </div>
                  <span className="px-2.5 py-1 rounded-lg bg-amber-100 text-amber-800 font-bold text-[11px]">
                    {item.left}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
